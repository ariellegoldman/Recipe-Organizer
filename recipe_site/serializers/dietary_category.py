from rest_framework import serializers
from recipe_site.models.dietary_category import DietaryCategory


class DietaryCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DietaryCategory
