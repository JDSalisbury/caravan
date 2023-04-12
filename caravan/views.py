from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Caravan, Job, Trader
from .serializers import CaravanSerializer, JobSerializer, TraderSerializer
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from django.db.models import Q
from django.db.models import Sum


class CaravanFilter(filters.FilterSet):
    biome = filters.CharFilter(field_name='biome')

    total_gold = filters.NumberFilter(
        field_name='total_gold', method='total_gold_filter')
    level = filters.NumberFilter(field_name='level')
    faculty = filters.CharFilter(field_name='faculty', method='faculty_filter')

    # def total_gold_filter(self, queryset, name, value):
    #     # sum of all traders' starting gold then filter by total gold
    #     return queryset.filter(Q(total_gold__lte=value)).aggergate(sum('traders__starting_gold'))

    def total_gold_filter(self, queryset, name, value):
        # filter by total gold
        # queryset = queryset.annotate(total_gold=Sum('traders__starting_gold'))
        # return queryset.filter(Q(total_gold__lte=value))
        return queryset.annotate(total_gold=Sum('traders__starting_gold')).filter(total_gold__lte=value)

    def faculty_filter(self, queryset, name, value):
        return queryset.filter(Q(traders__job__name=value))

    class Meta:
        model = Caravan
        fields = ['biome', 'faculty', 'level', 'total_gold']


class CaravanViewset(viewsets.ModelViewSet):
    queryset = Caravan.objects.all()
    serializer_class = CaravanSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CaravanFilter

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
