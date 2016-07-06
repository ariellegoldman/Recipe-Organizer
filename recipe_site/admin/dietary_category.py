from django.contrib import admin
from recipe_site.models.dietary_category import DietaryCategory


@admin.register(DietaryCategory)
class DietaryCategoryAdmin(admin.ModelAdmin):
    pass
