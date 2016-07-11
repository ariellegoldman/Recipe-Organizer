from rest_framework import serializers
from recipe_site.models.recipe import Recipe


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('dietary_category', 'url', 'name', 'id', 'ingredients', 'directions')
