from django.shortcuts import render

from recipe.models import RecipeItem, Author
from recipe.form import add_recipe

# Create your views here.
def index(request):
    data = RecipeItem.objects.all()
    author = Author.objects.all()
    return render(request, 'index.html', {'data': data, 'author':author})

def add_recipe(request):
    html = "add_recipe.html"
    
    breakpoint()
    
    form = add_recipe()

    return render(request, "add_recipe.html", {"form": form})


def author(request, id):
    data = RecipeItem.objects.all()
    author = Author.objects.get(id=id)
    recipe = RecipeItem.objects.filter(author=author)
    return render(request, 'author.html', {'data': data, 'author':author, 'recipe':recipe})

def recipe(request, id):
    # data = RecipeItem.objects.all()
    recipe = RecipeItem.objects.get(id=id)
    return render(request, 'recipe.html', {'recipe':recipe})


