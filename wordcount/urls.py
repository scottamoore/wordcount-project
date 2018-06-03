from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('views/', views.home),
    path('hello/', views.home, name="homepage"),
    path('count/', views.count, name="countpage"),
    path('about/', views.about, name="aboutpage"),
    path('', views.home),
]
