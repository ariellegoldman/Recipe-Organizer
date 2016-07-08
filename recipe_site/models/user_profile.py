from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    class Meta:
        app_label = "recipe_site_data"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourite = models.ManyToManyField("recipe_site_data.Recipe", blank=True)
