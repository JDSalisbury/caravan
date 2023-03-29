from django.db import models
from config.constants import CARAVAN_BIOMES
# Create your models here.


class Job(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Trader(models.Model):
    name = models.CharField(max_length=50)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    caravan = models.ForeignKey('Caravan', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.job})"

    def generate_items(self, level):
        # TODO: generate list of items based on trader's job and caravan level

        pass


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    rarity = models.PositiveIntegerField()
    job_requirements = models.ManyToManyField(Job)

    def __str__(self):
        return self.name


class Loot(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    items = models.ManyToManyField(Item)
    rarity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Caravan(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    biome = models.CharField(max_length=50, choices=CARAVAN_BIOMES)
    level = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.location})"


# generate list of traders based on biome and level and add them to the caravan, no duplicate jobs

    def generate_traders(self):
        trader_list = Trader.objects.filter(caravan__isnull=True)
        for trader in trader_list:
            if self.level >= trader.job.level_requirement and self.biome in trader.job.biomes:
                self.traders.add(trader)
                trader.caravan = self
                trader.save()
        return self.traders.all()
