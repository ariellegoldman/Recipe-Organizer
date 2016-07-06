from django.contrib import admin
from recipe_site.models.ingredient import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
