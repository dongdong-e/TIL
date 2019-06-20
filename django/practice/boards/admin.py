from django.contrib import admin
from .models import Board, Comment

### 게시판
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')

# models.py에 등록한 Board 클래스 호출
admin.site.register(Board, BoardAdmin)


### 댓글창
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at', 'updated_at')

# models.py에 등록한 Board 클래스 호출
admin.site.register(Comment, CommentAdmin)