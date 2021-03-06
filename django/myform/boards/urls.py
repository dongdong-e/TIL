from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create, name='create'),
    path('<int:board_pk>/', views.detail, name='detail'),
    path('<int:board_pk>/edit/', views.edit, name='edit'),
    path('<int:board_pk>/delete/', views.delete, name='delete'),
    path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:board_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:board_pk>/like/', views.like, name='like'),
    path('photo/', views.photo, name='photo'),
    path('screen/', views.screen, name='screent'),
    path('<int:board_pk>/follow/<int:user_pk>', views.follow, name='follow'),
]