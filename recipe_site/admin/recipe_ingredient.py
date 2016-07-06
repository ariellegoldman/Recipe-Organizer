from django.contrib import admin
from recipe_site.models.recipe_ingredient import RecipeIngredient


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    pass
