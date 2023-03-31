from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CaravanViewset, JobViewset, TraderViewset

router = DefaultRouter()

router.register('jobs', JobViewset)
router.register('caravans', CaravanViewset)
router.register('traders', TraderViewset)

urlpatterns = [
    path('random_traders/<int:pk>/',
         CaravanViewset.as_view({'get': 'random_traders'}), name='random_traders'),
] + router.urls
