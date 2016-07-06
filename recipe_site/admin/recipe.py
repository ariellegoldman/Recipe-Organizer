from django.contrib import admin
from recipe_site.models.recipe import Recipe
from recipe_site.models.recipe_ingredient import RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'directions', 'get_dietary_category', 'get_ingredients')
    inlines = RecipeIngredientInline,

    def get_ingredients(self, obj):
        g = ", ".join([g.name for g in obj.ingredients.all()])
        return "{0}".format(g)
    get_ingredients.short_description = "Ingredients"

    def get_dietary_category(self, obj):
        g = ", ".join([g.name for g in obj.dietary_category.all()])
        return "{0}".format(g)
    get_dietary_category.short_description = "Dietary Category"