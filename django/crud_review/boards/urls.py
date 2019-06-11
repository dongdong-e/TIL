from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('<int:pk>/', views.detail),
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/edit/', views.edit),
]