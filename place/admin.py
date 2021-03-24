
from django.contrib import admin

# Register your models here.
from place.models import Category, Place


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'location', 'city', 'country', 'status']
    list_filter = ['status', 'category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Place, PlaceAdmin)