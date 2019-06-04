from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('hola/', views.hola),
    path('dinner/', views.dinner),
    path('hello/<name>/', views.hello),
    path('introduce/<name>/<int:age>/', views.introduce),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('area/<int:num1>/', views.area),
    path('template_language/', views.template_language),
    path('birth_day/', views.birth_day),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('lotto/', views.lotto),
    path('lotto_number/', views.lotto_number),
    path('lotto_01/', views.lotto_01),
    path('get/', views.get),
    path('lotto_02/', views.lotto_02),
    path('pick_lotto/', views.pick_lotto),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]
