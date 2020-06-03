from django.urls import path

from recipe import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('add_author/', views.add_author, name='add_author'),
    path('author/<int:id>/', views.author, name='author'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
    path('edit<int:id>/', views.edit_recipe, name="edit"),
    path('favorite/<int:id>/', views.favorite, name='favorite'),
    path('unfavorite/<int:id>/', views.unfavorite, name='unfavorite'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
]
