from django.db import models


class Ingredient(models.Model):
    class Meta:
        app_label = "recipe_site_data"

    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name
