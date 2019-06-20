from django.db import models

### 게시판
class Board(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번글 - {self.title} : {self.content}'

### 댓글 기능
class Comment(models.Model):
    content = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}번글 - {self.title} : {self.content}'