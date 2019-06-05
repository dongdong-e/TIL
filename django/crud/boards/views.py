from django.shortcuts import render
from .models import Board

def index(request):
    # 장고는 기본적으로 templates 폴더에서 html 파일을 로딩한다.
    # 따라서, template 폴더가 위치한 boards 폴더에서 html 파일을 로딩해야 한다.
    context = Board.objects.all()
    return render(request, 'boards/index.html', {"Boards": context})


def new(request):
    return render(request, 'boards/new.html')


def create(request):
    # 'title'은 dictionary 형태이므로 get으로 string을 뽑아온다.
    title = request.GET.get('title')
    content = request.GET.get('content')

    board = Board(title=title, content=content)
    board.save()

    return render(request, 'boards/create.html')