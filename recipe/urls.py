from django.urls import path

from recipe import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('add_recipe/', views.add_recipe),
    path('add_author/', views.add_author),
    path('author/<int:id>/', views.author),
    path('recipe/<int:id>/', views.recipe),
    path('login/', views.loginview)
   # path('admin/', admin.site.urls),
]