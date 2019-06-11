from django.db import models


# 게시판 만들기
class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # <QuerySet [<Board: Board object (1)>, <Board: Board object (2)>]>
    # 이처럼 뜨는 DB 내용을 str 타입으로 보여주기 위한 함수
    # 함수 앞에 __(text)__ : magic method라고 불리며 특수한 기능을 가지고 있음
    def __str__(self):
        return f'{self.id}번글 - {self.title} : {self.content}'


# 댓글창 만들기
class Comment(models.Model):
    # 댓글 내용
    content = models.CharField(max_length=200)

    # 댓글 작성시간
    created_at = models.DateTimeField(auto_now_add=True)
    # 댓글 수정시간
    updated_at = models.DateTimeField(auto_now=True)

    # 댓글이 달린 게시글의 외래키 설정
    # on_delete=models.CASCADE: 게시글이 지워지면 댓글도 함께 지워짐
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Board {self.board_id}: Comment({self.id} - {self.content})>'