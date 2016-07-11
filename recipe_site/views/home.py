from django.contrib.auth.models import User
from rest_framework import views
from rest_framework.response import Response
from recipe_site.models.ingredient import Ingredient
from recipe_site.models.user_profile import UserProfile
from recipe_site.serializers.ingredient import IngredientSerializer
from recipe_site.models.dietary_category import DietaryCategory
from recipe_site.serializers.dietary_category import DietaryCategorySerializer
from recipe_site.serializers.user_profile import UserProfileSerializer


class HomeView(views.APIView):
    template_name = "index.jinja2"

    def get(self, request, *args, **kwargs):
        ingredients = Ingredient.objects.order_by('name')
        restrictions = DietaryCategory.objects.order_by('name')
        user_favourite = UserProfile.objects.order_by('id')
        user = User.objects.filter(username=request.user.username)

        ingredients_data = IngredientSerializer(ingredients,
                                            context={'request': request},
                                            many=True).data

        restrictions_data = DietaryCategorySerializer(restrictions,
                                                      context={'request': request},
                                                      many=True).data

        user_favourite_data = UserProfileSerializer(user_favourite.filter(user=user),
                                               context={'request': request}, many=True).data

        return Response({
            'ingredients': ingredients_data,
            'restrictions': restrictions_data,
            'user_favourite': user_favourite_data,
        })
