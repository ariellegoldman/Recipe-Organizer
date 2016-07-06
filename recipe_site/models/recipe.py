from django.db import models


class Recipe(models.Model):
    class Meta:
        app_label = "recipe_site_data"

    name = models.CharField(max_length=512)
    directions = models.TextField(blank=True, null=True)
    ingredients = models.ManyToManyField("recipe_site_data.Ingredient", through='RecipeIngredient')
    dietary_category = models.ManyToManyField("recipe_site_data.DietaryCategory", blank=True)

    def __str__(self):
        return self.name
