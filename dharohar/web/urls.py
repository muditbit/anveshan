from django.urls import path
from . import views
app_name = "web"

urlpatterns = [
    path('', views.home, name='home'),
    path("about/", views.about, name ='About Us'),
    path("search/", views.search, name ='Search'),
    path("index/", views.index, name='Index'),
    path("register/",views.register, name="register"),
]