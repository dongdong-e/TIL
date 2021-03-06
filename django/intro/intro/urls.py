from django.contrib import admin
from django.urls import path, include

# 끝에 항상 콤마 필수!
urlpatterns = [
    path('utilities/', include('utilities.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]