from django.db.models import Q
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
        ingredient_list = self.request.GET.getlist('ingredient')
        restriction_list = self.request.GET.getlist('restriction')
        print(ingredient_list)
        print(restriction_list)

        if ingredient_list:
            for ingredient in ingredient_list:
                queryset = queryset.filter(ingredients__name=ingredient)

        if restriction_list is not None:
            for restriction in restriction_list:
                restriction = restriction.split('_')
                queryset = queryset.filter(Q(dietary_category__name__icontains=restriction[0]), Q(dietary_category__name__icontains=restriction[1]))

        return queryset
