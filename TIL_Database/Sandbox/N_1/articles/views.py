from importlib.metadata import requires
import re
from tracemalloc import get_object_traceback
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    
    context = {
        'form': form,
    } 
    return render(request, 'articles/create.html', context)
    


def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(data=request.POST, instance=article)
            if form.is_valid():
                
    comment_form = CommentForm() # 댓글을 달기 위함
    comments = article.comment_set.all()
        # 1. 댓글을 보여주기 위한
        # 2. 역참조한거다!
    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


def comment_create(request, pk):
    # 데이터를 받을 판을 만들어 주는 것 (form)
    comment_form = CommentForm(request.POST)
    article = Article.objects.get(pk=pk) # article_pk

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save() # NOT NULL CONSTRAINS ??? article_id..?

    return redirect('articles:detail', article.pk)
    # GET -> 보여주기
    # POST -> 저장

# 기존 방식은 맞음
# def comments_delete(request, article_pk, comment_pk):
#     comment = Comment.objects.get(pk=comment_pk)
#     article_pk = comment.article.pk
#     comment.delete()
#     return redirect('articles:detail', article_pk)

# REST API를 위해서 URL의 일관성 지키자!
@require_POST
def comment_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)