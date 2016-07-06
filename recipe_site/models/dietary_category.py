from django.db import models


class DietaryCategory(models.Model):
    class Meta:
        app_label = "recipe_site_data"
        verbose_name_plural = "dietary categories"

    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name
