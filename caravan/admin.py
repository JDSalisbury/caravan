
from django.contrib import admin
from .models import Caravan, Trader, Item, Job, Biome
import pprint
from django.db.models import Q


class TraderAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'description',
                    'starting_gold', )
    list_filter = ('job', 'biomes')
    search_fields = ('name', 'job', 'description',
                     'starting_gold', 'biomes')
    # filter list of items by job

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "items":
            obj_id = request.resolver_match.kwargs.get('object_id')
            print(obj_id)
            trader = Trader.objects.get(id=obj_id)
            kwargs["queryset"] = Item.objects.filter(Q(job_requirements__name=trader.job) | Q(
                job_requirements__isnull=True) | Q(job_requirements__name='Trader'))
        return super().formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Caravan)
admin.site.register(Trader, TraderAdmin)
admin.site.register(Item)
admin.site.register(Job)
admin.site.register(Biome)
