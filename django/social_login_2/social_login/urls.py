from django.contrib import admin
from django.urls import path, include
import login.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', login.views.login, name='login'),
    path('accounts/', include('allauth.urls')),
    path('upload/', login.views.upload, name='upload'),
    path('delete/<int:upload_num>/', login.views.delete, name='delete'),
    path('set_phone_number/<int:upload_num>/', login.views.set_phone_number, name='set_phone_number'),
    path('confirm/<int:upload_num>/',login.views.confirm,name='confirm'),
    path('photo/<int:pk>/',login.views.photo, name='photo'),
    path('edit/<int:upload_num>/',login.views.edit, name='edit'),
    path('admin/', admin.site.urls),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)