from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from content.models import Content, CImages, Menu, Comment, UserPlaces, CImagess


# Register your models here.


class ContentImageInline(admin.TabularInline):
    model = CImages
    extra = 3

class MenuContentInline(admin.TabularInline):
    model = Content
    extra = 1

class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'image_tag', 'status', 'create_at']
    list_filter = ['status', 'type']
    inlines = [ContentImageInline]
    prepopulated_fields = {'slug': ('title',)}

class MenuAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title', 'status')
    list_filter = ['status']
    inlines = [MenuContentInline]



admin.site.register(Content, ContentAdmin)
admin.site.register(Menu, MenuAdmin)




################################################3
class UserPlacesImageInline(admin.TabularInline):
    model = CImagess
    extra = 3

class UserPlacesInline(admin.TabularInline):
    model = UserPlaces
    extra = 1

class UserPlacesAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'image_tag', 'status', 'create_at']
    list_filter = ['status', 'type']
    inlines = [UserPlacesImageInline]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(UserPlaces, UserPlacesAdmin)
