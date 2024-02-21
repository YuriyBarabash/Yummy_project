from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import FooterItem
from .models import DishCategory, Dish
from .models import Gallery
from .models import Reservation

admin.site.register(FooterItem)
admin.site.register(Reservation)


@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'position', 'is_visible')
    list_editable = ('name', 'position', 'is_visible')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'position', 'slug', 'ingredients', 'description', 'price','photo_src_tag','is_visible')
    list_editable = ('ingredients', 'price', 'position', 'is_visible')
    list_filter = ('category', 'is_visible')
    search_fields = ('name', 'ingredients', 'description')
    prepopulated_fields = {'slug': ('name',)}

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

    photo_src_tag.short_description = 'Dish photo'


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('photo', 'tittle', 'photo_src_tag','is_visible')
    list_editable = ('tittle', 'is_visible')
    list_filter = ('is_visible',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

    photo_src_tag.short_description = 'Image preview'




