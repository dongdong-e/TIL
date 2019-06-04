from django.urls import path
from . import views

# 끝에 항상 콤마 필수!
urlpatterns = [
    path('', views.index),
    path('random_photo', views.random_photo),
]