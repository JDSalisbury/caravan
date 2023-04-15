from rest_framework import serializers
from .models import Caravan, Item, Job, Trader, Biome


class BiomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biome
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class TraderDetailSerializer(serializers.ModelSerializer):
    job = JobSerializer()
    biomes = BiomeSerializer(many=True)
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Trader
        fields = ('name', 'job', 'biomes',
                  'description', 'starting_gold', 'items')


class TraderSerializer(serializers.ModelSerializer):
    job = JobSerializer()
    biomes = serializers.SlugRelatedField(
        slug_field='name', many=True, read_only=True)

    class Meta:
        model = Trader
        fields = ('id', 'name', 'job', 'biomes',
                  'description', 'starting_gold')


class CaravanSerializer(serializers.ModelSerializer):
    traders = TraderSerializer(many=True)

    class Meta:
        model = Caravan
        fields = ('id', 'name', 'location', 'biome',
                  'level',  'faculty', 'traders')
