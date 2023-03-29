from django.db import models

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
    biome = models.CharField(max_length=50, choices=(
        ('forest', 'Forest'),
        ('island', 'Island'),
        ('tropical', 'Tropical'),
        ('taiga', 'Taiga'),
        ('plateau', 'Plateau'),
        ('mountain', 'Mountain'),
        ('desert', 'Desert'),
        ('tundra', 'Tundra'),
        ('swamp', 'Swamp'),
        ('ocean', 'Ocean'),
        ('plains', 'Plains'),
        ('jungle', 'Jungle'),
        ('volcano', 'Volcano'),
        ('cave', 'Cave'),
        ('city', 'City'),
        ('castle', 'Castle'),
        ('dungeon', 'Dungeon'),
        ('ruins', 'Ruins'),
        ('graveyard', 'Graveyard'),
        ('cemetery', 'Cemetery'),
        ('temple', 'Temple'),
        ('church', 'Church'),
        ('library', 'Library'),
        ('school', 'School'),
        ('hospital', 'Hospital'),
        ('museum', 'Museum'),
        ('zoo', 'Zoo'),
        ('farm', 'Farm'),
        ('factory', 'Factory'),
        ('mine', 'Mine'),
        ('laboratory', 'Laboratory'),
    ))

    level = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.location})"

    def generate_traders(self):
        # TODO: generate list of traders based on biome and level
        pass
