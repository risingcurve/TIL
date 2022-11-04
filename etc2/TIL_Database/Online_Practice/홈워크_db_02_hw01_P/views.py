@ require_POST
def comment_create(request, article_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    article = get_object_or_404(Article, pk=__(a)__) # pk
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(__(b)__) # commit=False
        comment.author = __(c)__ # request.author
        comment.article = __(d)__ # article
        __(e)__ # comment.save()
        return redirect('articles:detail', article.pk)
    
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

