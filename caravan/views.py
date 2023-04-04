from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Caravan, Job, Trader
from .serializers import CaravanSerializer, JobSerializer, TraderSerializer
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters


class CaravanViewset(viewsets.ModelViewSet):
    queryset = Caravan.objects.all()
    serializer_class = CaravanSerializer

    @action(detail=True, methods=['get'])
    def random_traders(self, request, pk=None):
        caravan = self.get_object()
        caravan.generate_random_traders()
        serializer = self.get_serializer(caravan)
        return Response(serializer.data)


class JobViewset(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class TraderFilter(filters.FilterSet):
    job = filters.CharFilter(field_name='job__name')
    biome = filters.CharFilter(field_name='biomes__name')
    gold = filters.NumberFilter(field_name='starting_gold', lookup_expr='lte')
    starting_gold = filters.NumberFilter(field_name='starting_gold')
    # filter by description if null or not null

    description = filters.BooleanFilter(
        field_name='description', method='filter_description')

    def filter_description(self, queryset, name, value):
        print(value)
        if value is True:
            return queryset.filter(description__isnull=False)
        elif value is False:
            return queryset.filter(description__isnull=True)
        else:
            return queryset

    class Meta:
        model = Trader
        fields = ['job', 'biome', 'gold', 'starting_gold', 'description']


class TraderViewset(viewsets.ModelViewSet):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TraderFilter
