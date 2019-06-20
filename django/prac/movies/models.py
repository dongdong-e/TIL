from django.db import models

class Movie(models.Model):
    # 영화 제목(한글)
    title = models.CharField(max_length=100)

    # 영화 제목(영문)
    title_origin = models.CharField(max_length=100)

    # 투표수
    vote_count = models.IntegerField()

    # 개봉일
    open_date = models.CharField(max_length=100)

    # 장르
    genre = models.CharField(max_length=100)

    # 평점
    score = models.FloatField()

    # 포스터 이미지 url
    poster_url = models.TextField()

    # 영화 소개
    description = models.TextField()

    def __str__(self):
        return f'{self.id}번 영화 - {self.title} : {self.title_origin},' \
            f'{self.vote_count}, {self.open_date}, {self.genre}, {self.score},' \
            f'{self.score}, {self.poster_url}, {self.description}'