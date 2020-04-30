from django.shortcuts import render

from recipe.models import RecipeItem, Author

# Create your views here.
def index(request):
    data = RecipeItem.objects.all()
    return render(request, 'index.html', {'data': data})

def author(request):
    data = RecipeItem.objects.all()
    return render(request, 'author.html', {'data': data})

def recipe(request):
    data = RecipeItem.objects.all()
    return render(request, 'recipe.html', {'data': data})