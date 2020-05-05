from django.urls import path
from recipe import views

urlpatterns = [
    path('', views.index),
    path('add_recipe/<int:id>/', views.add_recipe, name="add_recipe"),
    path('author/<int:id>/', views.author, name='author'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
   # path('admin/', admin.site.urls),
]