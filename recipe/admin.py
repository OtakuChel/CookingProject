from django.contrib import admin
from .models import Product, Recipe, RecipeProduct

class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'uses')
    search_fields = ['name']

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('products',)
    inlines = [RecipeProductInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Recipe, RecipeAdmin)