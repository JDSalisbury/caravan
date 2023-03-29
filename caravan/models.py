from django.db import models
from config.constants import CARAVAN_BIOMES, ITEM_CATEGORIES
# Create your models here.


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

    def __str__(self):
        return self.name


class Caravan(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    biome = models.CharField(max_length=50, choices=CARAVAN_BIOMES)
    level = models.IntegerField()

    def __str__(self):
        return self.name

# generate list of traders based on biome and level and add them to the caravan, no duplicate jobs

    def generate_traders(self):
        trader_list = Trader.objects.filter(caravan__isnull=True)
        for trader in trader_list:
            if self.level >= trader.job.level_requirement and self.biome in trader.job.biomes:
                self.traders.add(trader)
                trader.caravan = self
                trader.save()
        return self.traders.all()

    def save(self, *args, **kwargs):
        # Check the number of traders with the same job
        for job in Job.objects.all():
            if self.traders.filter(job=job).count() > 1:
                raise ValueError('Too many traders with the same job')
        super().save(*args, **kwargs)


class Trader(models.Model):
    name = models.CharField(max_length=50)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    caravan = models.ForeignKey(Caravan, on_delete=models.CASCADE)
    starting_gold = models.PositiveIntegerField()

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
