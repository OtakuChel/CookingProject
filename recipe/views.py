from django.http import HttpResponse
from django.shortcuts import render
from recipe.models import RecipeProduct, Product, Recipe


def add_product_to_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')
        recipe = Recipe.objects.get(id=recipe_id)
        product = Product.objects.get(id=product_id)

        recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
        recipe_product.weight_in_grams = weight
        recipe_product.save()

        return HttpResponse("Продукт успешно добавлен в рецепт.")

def cook_recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
        recipe_products = RecipeProduct.objects.filter(recipe=recipe)
        for recipe_product in recipe_products:
            product = recipe_product.product
            product.uses += 1
            product.save()
    except Recipe.DoesNotExist:
        return HttpResponse(f"Рецепт с id {recipe_id} не найден")
    return HttpResponse("Количество использований продуктов из рецепта увеличено.")


def show_recipes_without_product(request, product_id):
    product = Product.objects.get(id=product_id)
    recipes_without_product = Recipe.objects.exclude(products=product)
    recipes_with_small_amount = Recipe.objects.filter(
        recipeproduct__product=product,
        recipeproduct__weight_in_grams__lt=10
    )
    context = {
        'product': product,
        'recipes_without_product': recipes_without_product,
        'recipes_with_small_amount': recipes_with_small_amount
    }
    return render(request, 'recipes_without_product.html', context)