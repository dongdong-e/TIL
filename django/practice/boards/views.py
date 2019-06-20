from django.shortcuts import render, redirect
from .models import Board, Comment


def index(request):
    boards = Board.objects.order_by('-id')
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)


def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        board = Board(title=title, content=content)
        board.save()
        return redirect('boards:index')
    else:
        return render(request, 'boards/new.html')


def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    comments = board.comment_set.all()

    context = {'board':board, 'comments':comments}
    return render(request, 'boards/detail.html', context)


def edit(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == "POST":
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()

        return redirect('boards:detail', board_pk)
    else:
        context = {'board':board}
        return render(request, 'boards/edit.html', context)

def delete(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == "POST":
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:index')

def comment_new(request, board_pk):
    content = request.POST.get('content')
    board = Board.objects.get(pk=board_pk)
    comment = Comment(content=content, board=board)
    comment.save()
    return redirect('boards:detail', board_pk)

def comment_edit(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    board = Board.objects.get(pk=board_pk)
    if request.method == "POST":
        comment.content = request.POST.get('content')
        comment.save()

        return redirect('boards:detail', board_pk)
    else:
        context = {'board':board, 'comment':comment}
        return render(request, 'boards/comment_edit.html', context)

