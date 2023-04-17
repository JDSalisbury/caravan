import csv
from ...models import Biome, Job, Item


def lower_case(string):
    return string.lower()


def capitalize(string):
    return string.capitalize()


def import_csv(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # create a new instance of the model and set its fields
            my_model = Item()
            my_model.name = row['name']
            my_model.description = row['description']
            my_model.price = int(row['price'])
            my_model.rarity = int(row['rarity'])
            my_model.category = row['category']
            my_model.damage_dice = row['damage_dice']
            my_model.damage_type = row['damage_type']
            my_model.critical = row['critical']
            my_model.armor_class = int(
                row['armor_class']) if row['armor_class'] else None
            my_model.armor_type = row['armor_type']
            my_model.property = row['property']
            my_model.power = row['power']
            my_model.save()

            # add related instances of Biome and Job if specified in the CSV
            biomes = row['biomes'].split(',') if row['biomes'] else []
            for biome_name in biomes:
                biome_name = lower_case(biome_name)
                try:
                    biome = Biome.objects.get(name=biome_name)
                    my_model.biomes.add(biome)
                except Biome.DoesNotExist:
                    biome = Biome(name=biome_name, description='Made from CSV')
                    biome.save()

            job_requirements = row['job_requirements'].split(
                ',') if row['job_requirements'] else []
            for job_name in job_requirements:
                job_name = capitalize(job_name)
                try:
                    job = Job.objects.get(name=job_name)
                    my_model.job_requirements.add(job)
                except Job.DoesNotExist:
                    job = Job(name=job_name, description='Made from CSV')
                    job.save()
