from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('gallery/', views.gallery, name='gallery'),
]