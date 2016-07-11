from rest_framework import generics
from rest_framework import renderers
from recipe_site.models.dietary_category import DietaryCategory
from recipe_site.serializers.dietary_category import DietaryCategorySerializer
from recipe_site.renderers.html_renderer import HTMLRenderer


class DietaryCategoryDetail(generics.RetrieveAPIView):
    template_name = "site/dietary_category.jinja2"
    queryset = DietaryCategory.objects.all()
    serializer_class = DietaryCategorySerializer
    renderer_classes = (HTMLRenderer, renderers.JSONRenderer)
