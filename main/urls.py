from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('about_me/', views.about_me)
]
