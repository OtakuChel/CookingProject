from django.urls import path, include
from . import views

urlpatterns = [
    #данные передаются через GET запрос (например, add_product_to_recipe/recipe_id=2&product_id=1&weight=200)
    path('add_product_to_recipe/', views.add_product_to_recipe),
    path('cook_recipe/<int:recipe_id>', views.cook_recipe, name='product'),
    path('show_recipes_without_product/<int:product_id>', views.show_recipes_without_product),
]