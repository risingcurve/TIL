import re
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
    comment_form = CommentForm() # 댓글을 달기 위한
    comments = article.comments.all() 
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
    if request.user.is_authenticated: # 로그인 했니?
        if request.user == article.user: # 작성자와 로그인 유저가 똑같아?    
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detial', article.pk)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(data=request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')        
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        # 데이터 받을 판을 만들어주는거 (form)
        comment_form = CommentForm(request.POST)
        article = Article.objects.get(pk=pk) # article_pk

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save() # NOT NULL CONSTRAINS ??? article_id..?
    
    return redirect('articles:detail', article.pk) 

# 기존 방식은 맞음
# def comments_delete(request,  comment_pk):
#     comment = Comment.objects.get(pk=comment_pk)
#     article_pk = comment.article.pk
#     comment.delete()
#     return redirect('articles:detail', article_pk)


# REST API를 위해서 url의 일관성 지키자!
@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)


def likes(request, article_pk):
    if request.user.is_authenticated:
        # 1. article 정보가 필요 <- article_pk
        article = get_object_or_404(Article, pk=article_pk)
    
        # 2. 게시글을 이미 좋아하고 있다 -> 좋아요 취소
        if article.like_users.filter(pk=request.user.pk).exists():
        # if request.user in article.like_users.all():
            article.like_users.remove(request.user)
        
        # 3. 게시글을 좋아하지 않았다 -> 좋아요 승인
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')

    return redirect('accounts:login')