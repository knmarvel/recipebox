from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from recipe.models import RecipeItem, Author
from recipe.forms import AddRecipeForm, AddAuthorForm, LoginForm


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(    
                    request.GET.get('next', reverse('homepage'))
                    )
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})

def index(request):
    data = RecipeItem.objects.all()
    author = Author.objects.all()
    return render(request, 'index.html', {'data': data, 'author': author})

@login_required
def add_recipe(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RecipeItem.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions'],
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddRecipeForm()
    
    return render(request, html, {'form': form})

@login_required
def add_author(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    
    form = AddAuthorForm()

    return render(request, html, {'form': form})

def author(request, id):
    data = RecipeItem.objects.all()
    author = Author.objects.get(id=id)
    recipe = RecipeItem.objects.filter(author=author)
    return render(request, 'author.html', {'data' : data, 'author' :author, 'recipe' :recipe})

def recipe(request, id):
    # data = RecipeItem.objects.all()
    recipe = RecipeItem.objects.get(id=id)
    return render(request, 'recipe.html', {'recipe':recipe})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
    # return HttpResponseRedirect(reverse('logoutURL'))



