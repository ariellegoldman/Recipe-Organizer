from django.db.models import Q
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from rest_framework import generics
from rest_framework import renderers
from rest_framework.reverse import reverse
from recipe_site.models.recipe import Recipe
from recipe_site.models.user_profile import UserProfile
from recipe_site.renderers.html_renderer import HTMLRenderer
from recipe_site.serializers.recipe import RecipeSerializer


class RecipeDetail(generics.RetrieveAPIView):
    template_name = "site/recipe.jinja2"
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    renderer_classes = (HTMLRenderer, renderers.JSONRenderer)

    def post(self, request, *args, **kwargs):

        favourite = request.POST['favourite']
        profile_id = request.POST['current_user']
        current_url = request.POST['from']
        if favourite:
            print(favourite)
            user_favourite = UserProfile.objects.get(id=profile_id)
            print(user_favourite.favourite.all())

            #check if it's already a favourite
            try:
                user_favourite.favourite.add(favourite)
            except IntegrityError:
                return HttpResponseRedirect(reverse("home"))

            return HttpResponseRedirect(reverse("home"))

        return HttpResponseRedirect(current_url)


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
                if "_" in restriction:
                    restriction = restriction.split('_')
                queryset = queryset.filter(Q(dietary_category__name__icontains=restriction[0]), Q(dietary_category__name__icontains=restriction[1]))

        return queryset
