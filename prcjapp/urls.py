from django.urls import path
from prcjapp import views

urlpatterns = [
    #path("", views.home, name="home"),
      path("prac/", views.prac,name="prac"),
]