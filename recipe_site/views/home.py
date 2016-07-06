from rest_framework import views
from rest_framework.response import Response
from recipe_site.models.ingredient import Ingredient
from recipe_site.serializers.ingredient import IngredientSerializer
from recipe_site.models.dietary_category import DietaryCategory
from recipe_site.serializers.dietary_category import DietaryCategorySerializer


class HomeView(views.APIView):
    template_name = "index.jinja2"

    def get(self, request, *args, **kwargs):
        ingredients = Ingredient.objects.order_by('name')
        restrictions = DietaryCategory.objects.order_by('name')
        ingredients_data = IngredientSerializer(ingredients,
                                            context={'request': request},
                                            many=True).data
        restrictions_data = DietaryCategorySerializer(restrictions,
                                                      context={'request': request},
                                                      many=True).data

        return Response({
            'ingredients': ingredients_data,
            'restrictions': restrictions_data,
        })
