# Generated by Django 4.1.7 on 2023-04-04 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caravan', '0004_alter_biome_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='trader',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='biome',
            name='name',
            field=models.CharField(choices=[('any', 'Any'), ('forest', 'Forest'), ('island', 'Island'), ('tropical', 'Tropical'), ('taiga', 'Taiga'), ('plateau', 'Plateau'), ('mountain', 'Mountain'), ('desert', 'Desert'), ('tundra', 'Tundra'), ('swamp', 'Swamp'), ('ocean', 'Ocean'), ('plains', 'Plains'), ('jungle', 'Jungle'), ('volcano', 'Volcano'), ('cave', 'Cave'), ('city', 'City'), ('castle', 'Castle'), ('dungeon', 'Dungeon'), ('ruins', 'Ruins'), ('graveyard', 'Graveyard'), ('cemetery', 'Cemetery'), ('temple', 'Temple'), ('church', 'Church'), ('library', 'Library'), ('school', 'School'), ('hospital', 'Hospital'), ('museum', 'Museum'), ('zoo', 'Zoo'), ('farm', 'Farm'), ('factory', 'Factory'), ('mine', 'Mine'), ('laboratory', 'Laboratory')], max_length=50),
        ),
        migrations.AlterField(
            model_name='caravan',
            name='biome',
            field=models.CharField(choices=[('any', 'Any'), ('forest', 'Forest'), ('island', 'Island'), ('tropical', 'Tropical'), ('taiga', 'Taiga'), ('plateau', 'Plateau'), ('mountain', 'Mountain'), ('desert', 'Desert'), ('tundra', 'Tundra'), ('swamp', 'Swamp'), ('ocean', 'Ocean'), ('plains', 'Plains'), ('jungle', 'Jungle'), ('volcano', 'Volcano'), ('cave', 'Cave'), ('city', 'City'), ('castle', 'Castle'), ('dungeon', 'Dungeon'), ('ruins', 'Ruins'), ('graveyard', 'Graveyard'), ('cemetery', 'Cemetery'), ('temple', 'Temple'), ('church', 'Church'), ('library', 'Library'), ('school', 'School'), ('hospital', 'Hospital'), ('museum', 'Museum'), ('zoo', 'Zoo'), ('farm', 'Farm'), ('factory', 'Factory'), ('mine', 'Mine'), ('laboratory', 'Laboratory')], max_length=50),
        ),
    ]
