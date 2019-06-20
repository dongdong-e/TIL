from django.db import models
from django.conf import settings

class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # USER와 게시글의 1:M 관계 만들기
    # AUTH_USER_MODEL
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='like_boards',
                                        blank=True)

    # board.user: 게시글을 작성한 유저
    # board.like_users: 게시글을 좋아요한 유저
    # user.board_set.all(): 유저가 작성한 모든 게시글
    # user.like_boards: 유저가 좋아요한 게시글


    def __str__(self):
        return f'글 번호: {self.id}, 글 제목: {self.title}, 글 내용: {self.content}'


class Comment(models.Model):
    content = models.CharField(max_length=100)
    # USER와 댓글의 1:M 관계 만들기
    # AUTH_USER_MODEL
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    # class Meta:
    #     ordering = ('-pk',)