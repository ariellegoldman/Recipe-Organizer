from rest_framework import serializers
from recipe_site.models.ingredient import Ingredient


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
