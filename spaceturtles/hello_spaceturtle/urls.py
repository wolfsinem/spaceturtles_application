from django.urls import path
from hello_spaceturtle import views

urlpatterns = [
    path('', views.hello_world, name='hello_spaceturtle'),
]