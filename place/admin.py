
from django.contrib import admin

# Register your models here.
from place.models import Category, Place, Images

class PlaceImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'location', 'city', 'country', 'status']
    list_filter = ['status', 'category']
    inlines = [PlaceImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'place', 'image']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Images, ImagesAdmin)