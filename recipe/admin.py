from django.contrib import admin
from recipe.models import Author, RecipeItem

# Register your models here.
admin.site.register(Author)
admin.site.register(RecipeItem)
