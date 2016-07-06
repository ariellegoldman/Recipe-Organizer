from rest_framework import generics
from rest_framework import renderers
from recipe_site.models.ingredient import Ingredient
from recipe_site.serializers.ingredient import IngredientSerializer
from recipe_site.renderers.html_renderer import HTMLRenderer


class IngredientDetail(generics.RetrieveAPIView):
    template_name = "site/ingredient.jinja2"
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    renderer_classes = (HTMLRenderer, renderers.JSONRenderer)
