from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles, 
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html', )

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    #1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2.
    article = Article(title=title, content=content)
    article.save()

    #3.
    # 안쓰는 편
    # 유효성 검사(post)
    # article.objects.create(title=title, content=content)

    # return render(request, 'articles/index.html')
    # return redirect('articles:index')
    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    # article = Article.objects.get(pk=pk)
    # article.delete() # 삭제는 바로 삭제됨.
    # return redirect('articles:index')
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')

        
    # request.method == 'GET'
    # datail로 다시 가!
    
    return render(request, 'articles/whoru.html')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)