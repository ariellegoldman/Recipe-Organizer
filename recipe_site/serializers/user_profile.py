from rest_framework import serializers
from recipe_site.models.user_profile import UserProfile
from recipe_site.models.recipe import Recipe


class RecipeUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = 'name', 'url'


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    favourite = RecipeUserProfileSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ('id','favourite')

