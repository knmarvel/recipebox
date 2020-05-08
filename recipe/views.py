from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

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
    form = AddAuthorForm()
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Matt Perry assisted with this portion of extending the addauthor to include user
            new_user = User.objects.create_user(
                username=data['name'] 
            )
            
            new_author = Author.objects.create(
                name=data['name'],bio=data['bio'],user=new_user)
            new_author.save()
            return HttpResponseRedirect(reverse('homepage'))    

    
    if request.user.is_staff:
        return render(request, html, {'form': form})
    return render(request, 'no_access.html')

def author(request, id):
    data = RecipeItem.objects.all()
    author = Author.objects.get(id=id)
    recipe = RecipeItem.objects.filter(author=author)
    return render(request, 'author.html', {'data' : data, 'author' :author, 'recipe' :recipe})

def recipe(request, id):
    recipe = RecipeItem.objects.get(id=id)
    return render(request, 'recipe.html', {'recipe':recipe})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
    



