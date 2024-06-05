from django.contrib import admin
from .models import *
from adminsortable2.admin import SortableAdminMixin


@admin.register(Roadmap)
class RoadmapAdmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ['id', 'roadmap_name', 'roadmap_slug', 'roadmap_image']
# Register your models here.
admin.site.register(Topic)
admin.site.register(Subtopic)