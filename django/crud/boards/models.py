from django.db import models

# 게시판 만들기
class Board(models.Model):
    # 제목
    # CharField -> max_length: 글자수 제한 설정
    title = models.CharField(max_length=10)

    # 내용
    content = models.TextField()

    # 게시글 작성시간
    # DateTimeField -> auto_now_add: 최초작성 시간 (불변)
    created_at = models.DateTimeField(auto_now_add=True)

    # 게시글 수정시간
    # DateTimeField -> auto_now: 수정 시간 (가변)
    updated_at = models.DateTimeField(auto_now=True)

    # <QuerySet [<Board: Board object (1)>, <Board: Board object (2)>]>
    # 이처럼 뜨는 DB 내용을 str 타입으로 보여주기 위한 함수
    # 함수 앞에 __(text)__ : magic method라고 불리며 특수한 기능을 가지고 있음
    def __str__(self):
        return f'{self.id}번글 - {self.title} : {self.content}'