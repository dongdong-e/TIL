from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm
from IPython import embed


def index(request):
    boards = Board.objects.order_by('-id')
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)

def create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        # embed()
        ## 유효성 검사 단계: Null값이나 type 오류를 찾아냄
        ## is_valid(): True / False 형태로 결과를 나타냄
        if form.is_valid():
            board = form.save()
            ## cleaned_data: True / False를 정제해서 나타냄
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # board = Board.objects.create(title=title, content=content)
            return redirect('boards:detail', board.pk)

    else:
        form = BoardForm()
    context = {'form':form}
    return render(request, 'boards/form.html', context)


def detail(request, board_pk):
    # board = Board.objects.get(pk=board_pk)
    board = get_object_or_404(Board, pk=board_pk)
    context = {'board':board}
    return render(request, 'boards/detail.html', context)


def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == "POST":
        board.delete()
        return redirect('boards:index')

    context = {'board':board}
    return render(request, 'boards/detail.html', context)
    # else:
    #     context = {'board':board}
    #     return render(request, 'boards/detail.html', context)


def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            # board.title = form.cleaned_data.get('title')
            # board.content = form.cleaned_data.get('content')
            # board.save()
            return redirect('boards:detail', board.pk)
    else:
        # initial=board.__dict__: 기존에 사용자가 작성한 text를 불러오는 함수
        form = BoardForm(instance=board)
    context = {'form': form, 'board':board}
    return render(request, 'boards/form.html', context)



def photo(request):
    return render(request, 'boards/photo.html')