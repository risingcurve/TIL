from django.db import models
from django.conf import settings # 직접 가져오지 않고 ... settings 에서 가져온다

'''
1. 게시글을 작성한 유저 -> N:1
    - article.user
    유저가 작성한 게시글들(역참조) -> 1:N
    - user.article_set


2. 게시글을 좋아한 유저 -> M:N
    - article.like_users
    유저가 좋아요한 게시글들(역참조) -> N:M
    - user.like_articles
    
'''
class Article(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # comment_set 
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments') # article_id
    # 1. 참조할 테이블(객체/모델) 이름 
    # 2. on_delete = 
        # models.CASCADE
        # NO_USER_NAME <- SET_DEAFULT
    # 3. related_name = 
        # 나를 참조하는 테이블(객체/모델)에서 조회할때 나오는 이름
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content



