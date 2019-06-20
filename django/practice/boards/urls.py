from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:board_pk>/detail/', views.detail, name='detail'),
    path('<int:board_pk>/edit/', views.edit, name='edit'),
    path('<int:board_pk>/delete/', views.delete, name='delete'),
    path('<int:board_pk>/detail/comment_new/', views.comment_new, name='comment_new'),
    path('<int:board_pk>/detail/comment_edit/<int:comment_pk>', views.comment_edit, name='comment_edit'),
]