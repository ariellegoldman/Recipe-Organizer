from django.db import models


class RecipeIngredient(models.Model):
    class Meta:
        app_label = "recipe_site_data"

    amount = models.CharField(max_length=512)
    ingredient = models.ForeignKey("recipe_site_data.Ingredient")
    recipe = models.ForeignKey("recipe_site_data.Recipe")

