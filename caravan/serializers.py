from rest_framework import serializers
from .models import Caravan, Job, Trader


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class TraderSerializer(serializers.ModelSerializer):
    job = JobSerializer()

    class Meta:
        model = Trader
        fields = ('id', 'name', 'job',)


class CaravanSerializer(serializers.ModelSerializer):
    traders = TraderSerializer(many=True)

    class Meta:
        model = Caravan
        fields = ('id', 'name', 'location', 'biome', 'level', 'traders')
