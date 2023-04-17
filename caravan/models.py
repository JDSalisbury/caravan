from django.db import models
from config.constants import CARAVAN_BIOMES, ITEM_CATEGORIES
# Create your models here.
from django.db.models import Q


class Biome(models.Model):
    name = models.CharField(max_length=50, choices=CARAVAN_BIOMES)
    description = models.TextField()

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    rarity = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=ITEM_CATEGORIES)
    damage_dice = models.CharField(max_length=10, null=True, blank=True)
    damage_type = models.CharField(max_length=50, null=True, blank=True)
    critical = models.CharField(max_length=50, null=True, blank=True)
    armor_class = models.IntegerField(null=True, blank=True)
    armor_type = models.CharField(max_length=50, null=True, blank=True)
    property = models.CharField(max_length=50, null=True, blank=True)
    power = models.CharField(max_length=50, null=True, blank=True)
    biomes = models.ManyToManyField(Biome, blank=True)
    job_requirements = models.ManyToManyField(Job, blank=True)

    def __str__(self):
        return self.name


class Caravan(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    biome = models.CharField(max_length=50, choices=CARAVAN_BIOMES)
    level = models.IntegerField()
    traders = models.ManyToManyField('Trader', blank=True)

    @property
    def faculty(self):
        return [trader.job.name for trader in self.traders.all()]

    def __str__(self):
        return self.name

    def generate_random_traders(self, num_traders=3):
        print('generating random traders')
        traders = set()
        while len(traders) < num_traders:
            trader = Trader.objects.filter(
                Q(biomes__name=self.biome) | Q(biomes__name='any')).order_by('?').first()
            if trader.job not in [trader.job for trader in traders]:
                traders.add(trader)
            if len(traders) > num_traders:
                traders.pop()
        self.traders.set(traders)
        self.save()


class Trader(models.Model):
    name = models.CharField(max_length=50)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    starting_gold = models.PositiveIntegerField()
    biomes = models.ManyToManyField(Biome)
    description = models.TextField(blank=True, null=True)
    items = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return self.name

    def total_price(self):
        return sum(item.price for item in self.items.all())

    def generate_random_items(self, num_items=10):
        print('generating random items')
        items = set()
        while len(items) < num_items:
            item = Item.objects.filter(
                Q(job_requirements__name=self.job) | Q(job_requirements__isnull=True) | Q(job_requirements__name='Trader')).order_by('?').first()
            if item not in items:
                items.add(item)
            if len(items) > num_items:
                items.pop()
        self.items.set(items)
        self.save()

    def generate_items(self):
        items = []
        for item in Item.objects.filter(rarity__lte=self.caravan.level):
            if self.job in item.job_requirements:
                items.append(item)
            elif item.job_requirements is None:
                items.append(item)
        return items

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.biomes.count() == 0:
            self.biomes.add(Biome.objects.get(name='any'))

        if 'any' in self.biomes.values_list('name', flat=True):
            self.biomes.clear()
            super().save(*args, **kwargs)

            self.biomes.set([Biome.objects.get(name='any')])
        super().save(*args, **kwargs)


class caravan_trader_items(models.Model):
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.trader} - {self.item} - {self.count}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('trader', 'item')
        # db_table = 'caravan_trader_items'
