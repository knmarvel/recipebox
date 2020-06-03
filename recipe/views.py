from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from recipe.models import RecipeItem, Author
from recipe.forms import AddRecipeForm, AddAuthorForm
from recipe.forms import LoginForm, NotStaffRecipeForm


def index(request):
    data = RecipeItem.objects.all()
    author = Author.objects.all()
    return render(request, 'index.html', {'data': data, 'author': author})


def author(request, id):
    data = RecipeItem.objects.all()
    author = Author.objects.get(id=id)
    recipe = RecipeItem.objects.filter(author=author)
    return render(request, 'author.html', {
        'data': data, 'author': author, 'recipe': recipe
        })


def recipe(request, id):
    recipe = RecipeItem.objects.get(id=id)
    fav = False
    if request.user.is_authenticated:
        if request.user in Author.user.get_queryset():
            author = Author.objects.get(user=request.user)
            if recipe in author.favorites.all():
                fav = True
    return render(request, 'recipe.html', {
        'recipe': recipe,
        'fav': fav
        })


@login_required
def favorite(request, id):
    this_recipe = RecipeItem.objects.get(id=id)
    author = Author.objects.get(user=request.user)
    author.favorites.add(this_recipe)
    author.save()
    return redirect(recipe, id=this_recipe.id)


@login_required
def unfavorite(request, id):
    this_recipe = RecipeItem.objects.get(id=id)
    author = Author.objects.get(user=request.user)
    author.favorites.remove(this_recipe)
    author.save()
    return redirect(recipe, id=this_recipe.id)


@login_required
def add_recipe(request):
    html = "generic_form.html"
    form = AddRecipeForm()
    if request.user.is_staff:
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
    if not request.user.is_staff:
        form = NotStaffRecipeForm(request.POST)
        if request.method == "POST" and form.is_valid():
            data = form.cleaned_data
            RecipeItem.objects.create(
                title=data['title'],
                author=request.user.author,
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions'],
            )
            return HttpResponseRedirect(reverse('homepage'))
        form = NotStaffRecipeForm()
    return render(request, html, {'form': form})


@login_required
def add_author(request):
    html = "generic_form.html"
    form = AddAuthorForm()
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Matt Perry assisted with this portion new_user
            new_user = User.objects.create_user(
                username=data['name'], password=data['password']
            )
            new_author = Author.objects.create(
                name=data['name'], bio=data['bio'], user=new_user)
            new_author.save()
            return HttpResponseRedirect(reverse('homepage'))

    if request.user.is_staff:
        return render(request, html, {'form': form})
    return render(request, 'no_access.html')


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


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
