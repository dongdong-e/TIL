# 필요한 라이브러리 호출
from django.shortcuts import render, redirect
from .models import Board # models.py에 있는 Board class 호출

# 함수 만들기
def index(request):
    # 장고는 기본적으로 templates 폴더에서 html 파일을 로딩한다.
    # 따라서, template 폴더가 위치한 boards 폴더에서 html 파일을 로딩해야 한다.
    # boards = Board.objects.order_by('-id')
    boards = Board.objects.all()[::-1]
    context = {'Boards': boards}
    return render(request, 'boards/index.html', context)


# new: 사용자가 글을 입력하기 위한 함수
def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        board = Board(title=title, content=content)
        board.save()
        return redirect(f'/boards/{board.pk}/')
    else:
        return render(request, 'boards/new.html')


def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board': board}

    return render(request, 'boards/detail.html', context)


# 게시글을 삭제하는 함수
def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()

    return redirect('/boards/')

# 게시글을 수정하는 함수
def edit(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board': board}

    return render(request, 'boards/edit.html', context)

def update(request, pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()

    return redirect(f'/boards/{board.pk}/')