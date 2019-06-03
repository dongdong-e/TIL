"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from pages import views

# 끝에 항상 콤마 필수!
urlpatterns = [
    path('admin/', admin.site.urls),
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
]