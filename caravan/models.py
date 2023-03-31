from django.db import models
from config.constants import CARAVAN_BIOMES, ITEM_CATEGORIES
# Create your models here.

# TODO: Create a way to link Biome to Types of Items that could show up, and possible types of traders selling said items


class Biome(models.Model):
    name = models.CharField(max_length=50, choices=ITEM_CATEGORIES)
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
    job_requirements = models.ManyToManyField(Job)
    category = models.CharField(max_length=50, choices=ITEM_CATEGORIES)
    damage_dice = models.CharField(max_length=10, null=True, blank=True)
    damage_type = models.CharField(max_length=50, null=True, blank=True)
    critical = models.CharField(max_length=50, null=True, blank=True)
    armor_class = models.IntegerField(null=True, blank=True)
    armor_type = models.CharField(max_length=50, null=True, blank=True)
    property = models.CharField(max_length=50, null=True, blank=True)
    power = models.CharField(max_length=50, null=True, blank=True)
    biomes = models.ManyToManyField(Biome)

    def __str__(self):
        return self.name


class Caravan(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    biome = models.CharField(max_length=50, choices=CARAVAN_BIOMES)
    level = models.IntegerField()
    traders = models.ManyToManyField('Trader', blank=True)

    def __str__(self):
        return self.name

# generate list of traders based on biome and level and add them to the caravan, no duplicate jobs

    def generate_random_traders(self, num_traders=3):
        traders = set()
        while len(traders) < num_traders:
            trader = Trader.objects.all().order_by('?').first()
            if trader.job not in [trader.job for trader in traders]:
                traders.add(trader)

        self.traders.set(traders)
        self.save()


class Trader(models.Model):
    name = models.CharField(max_length=50)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    starting_gold = models.PositiveIntegerField()
    biomes = models.ManyToManyField(Biome)

    def __str__(self):
        return self.name

    def total_price(self):
        return sum(item.price for item in self.items.all())

    def generate_items(self):
        items = []
        for item in Item.objects.filter(rarity__lte=self.caravan.level):
            if self.job in item.job_requirements:
                items.append(item)
            elif item.job_requirements is None:
                items.append(item)
        return items
