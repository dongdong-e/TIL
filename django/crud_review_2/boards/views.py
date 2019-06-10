# 라이브러리 import
from django.shortcuts import render, redirect
from .models import Board


def index(request):
    boards = Board.objects.order_by('-id')
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)


def new(request):
    return render(request, 'boards/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    board = Board(title=title, content=content)
    board.save()

    # HTML: /boards/{{ board.pk }}/
    # python: f'/boards/{board.pk}/
    # 위에 둘은 같은 기능
    return redirect(f'/boards/{board.pk}/')


def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board':board}
    return render(request, 'boards/detail.html', context)


def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('/boards/')


def edit(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board':board}
    return render(request, 'boards/edit.html', context)


def update(request, pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()

    return redirect(f'/boards/{board.pk}/')