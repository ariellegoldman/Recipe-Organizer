"""recipe_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from recipe_site.views.auth import SessionAuth, SessionClose
from recipe_site.views.home import HomeView
from recipe_site.views.ingredient import IngredientDetail
from recipe_site.views.dietary_category import DietaryCategoryDetail
from recipe_site.views.recipe import RecipeDetail, RecipeList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^ingredients/(?P<pk>[0-9]+)/$', IngredientDetail.as_view(), name="ingredient-detail"),
    url(r'^dietary-categories/(?P<pk>[0-9]+)/$', DietaryCategoryDetail.as_view(), name="dietarycategory-detail"),
    url(r'^recipe/(?P<pk>[0-9]+)/$', RecipeDetail.as_view(), name="recipe-detail"),
    url(r'^recipes/$', RecipeList.as_view(), name="recipe-list"),
    url(r'^login/$', SessionAuth.as_view(), name="login"),
    url(r'^logout/$', SessionClose.as_view(), name="logout"),
]
