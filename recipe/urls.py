from django.urls import path
from recipe import views

urlpatterns = [
    path('', views.index),
    path('', views.author),
    path('', views.recipe),
   # path('admin/', admin.site.urls),
]