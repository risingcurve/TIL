from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    issue_a = models.CharField(max_length=50)
    issue_b = models.CharField(max_length=50)


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 1. 참조할 모델
    # 2. on_delete = models.CASCADE
    # 3. related_name (선택사항)
    content = models.CharField(max_length=100)
    pick = models.BooleanField()
