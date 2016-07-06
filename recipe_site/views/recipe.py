from rest_framework import generics
from rest_framework import renderers
from recipe_site.models.recipe import Recipe
from recipe_site.renderers.html_renderer import HTMLRenderer
from recipe_site.serializers.recipe import RecipeSerializer


class RecipeDetail(generics.RetrieveAPIView):
    template_name = "site/recipe.jinja2"
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    renderer_classes = (HTMLRenderer, renderers.JSONRenderer)


class RecipeList(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    template_name = "site/recipe_list.jinja2"
    renderer_classes = (HTMLRenderer, renderers.JSONRenderer)

    def get_queryset(self):
        queryset = Recipe.objects.all()
        ingredient = self.request.query_params.get('ingredient', None)
        if ingredient is not None:
            queryset = queryset.filter(ingredients__name=ingredient)
        return queryset
