from django.db import models



class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Board(models.Model):
    title = models.CharField(max_length=20)

    # User 클래스의 pk를 적용시키기
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    content = models.CharField(max_length=100)

    # Board 클래스의 pk 적용시키기
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    # User 클래스의 pk를 적용시키기
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content}'

