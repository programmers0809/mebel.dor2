from django.contrib import admin
from .models import ProductModel, OneModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price')
    search_fields = ('name', 'brand')  # Qidiruv maydoni
    list_filter = ('brand', 'price')  # Filtr qo‘shildi
    ordering = ('price',)  # Narx bo‘yicha tartib


@admin.register(OneModel)
class OneModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)
    prepopulated_fields = {'name': ('name',)}  # Slug yaratish uchun
