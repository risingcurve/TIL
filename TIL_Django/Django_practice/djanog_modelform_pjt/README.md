# PJT 05

### 이번 pjt 를 통해 배운 내용

* 장고 모델폼 활용 방법

## 0. 공통 요구사항

* 요구 사항 :
  • 커뮤니티 웹 서비스의 데이터 구성 단계입니다.
  • 영화 데이터의 생성, 조회, 수정, 삭제가 가능한 애플리케이션을 완성합니다.
  • Django 프로젝트의 이름은 mypjt, 앱이름은 movies로 지정합니다.
  • .gitignore 파일을 추가하여 불필요한 파일 및 폴더는 제출하지 않도록 합니다.
  • 명시된 요구사항 이외에는 자유롭게 작성해도 무관합니다.

  * 문제 접근 방법 및 코드 설명

```
# models.py

from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title
```

```
# movies/url.py

from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),  
]
```


```
# views.py

from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies, 
    }
    return render(request, 'movies/index.html', context)


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

    
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/detail.html', context)


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')
```

```
# forms.py

from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    comedy = 'comedy'
    horror = 'horror'
    romance = 'romance'

    GENRE_CHOICE = [
        (comedy, '코미디'),
        (horror, '공포'),
        (romance, '로맨스'),
    ]

    genre = forms.ChoiceField(
        label = 'Genre',
        choices = GENRE_CHOICE,
        widget = forms.Select()
    )

    release_date = forms.DateField(
        widget = forms.DateInput(
            attrs = {
                'type': 'date',
            }
        )
    )

    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'step': 0.5,
                'min': 0,
                'max': 5,
                'placeholder': 'Score',
            }
        )
    )

    class Meta:
        model = Movie
        fields = '__all__'
```

* 이 문제에서 어려웠던점 : 
* 내가 생각하는 이 문제의 포인트 : 모델폼에 맞게 함수를 코딩하는 것.



## A. base.html

* 요구 사항 :
• 공통 부모 템플릿
  • 모든 템플릿 파일은 base.html을 상속 받아 사용합니다.
  • Bootstrap 사용을 위한 코드를 삽입합니다.

* 결과 :

  * 문제 접근 방법 및 코드 설명 : 부트스트랩 cdn을 넣어서 요구사항을 그대로 구현했습니다.

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  <style>
    body {
      margin-bottom: 30px;
    }
  </style>
</head>
<body>
  <div class="container">
    {% block  content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>

```
* 이 문제에서 어려웠던점 : 없음.
* 내가 생각하는 이 문제의 포인트 : cdn 삽입




## B. index.html

* 요구 사항 :
• “전체 영화 목록 조회 페이지”
  • 데이터 베이스에 존재하는 모든 영화의 목록을 표시합니다.
  • 적절한 HTML 요소를 사용하여 영화 제목 및 평점을 표시하며, 제목을 클릭 시 해당 영화의 상세 조회 페이지(detail.html)로 이동합니다.

* 결과 :

  * 문제 접근 방법 및 코드 설명 : url -> views -> index로 정보가 넘어올 수 있도록 코드 작성.

```
{% extends 'base.html' %}

{% block content %}
  <h1>INDEX</h1>
  <a href="{% url 'movies:create' %}">[CREATE]</a>
  <hr>
  {% for movie in movies %}
      <a href="{% url 'movies:detail' movie.pk %}">

        <h5>{{ movie.title }}</h5>

      </a>
      <p>{{ movie.score }}</p>
      <hr>
    {% endfor %}
{% endblock content %}
```
* 이 문제에서 어려웠던점 : 딱히 없었습니다.
* 내가 생각하는 이 문제의 포인트 : index로 잘 받아올 수 있는가



## C. detail.html

* 요구 사항 :
• “영화 상세 정보 페이지”
• 특정 영화의 상세 정보를 표시합니다.
• Bootstrap Card Component를 사용합니다.
• 해당 영화의 수정 및 삭제 버튼을 표시합니다.
• 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크를 표시합니다.

* 결과 :

  * 문제 접근 방법 및 코드 설명 : 영화의 정보를 담아내기 위해 html 태그와 부트스트랩을 이용하여 화면 구성.

```
{% extends 'base.html' %}

{% block content %}
<h2 style="text-align: center;">DETAIL</h2>
<hr>
  <div class="card" style="width: 18rem; margin: auto">
    <img src="{{ movie.poster_url }}" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{{ movie.title }}</h5>
      <p class="card-text">Audience : {{ movie.audience }}</p>
      <p class="card-text">Release Dates : {{ movie.release_date }}</p>
      <p class="card-text">Genre : {{ movie.genre }}</p>
      <p class="card-text">Score : {{ movie.score }}</p>
      <p class="card-text">시실리에서 이민온 뒤, 정치권까지 영향력을 미치는 거물로 자리잡은 돈 꼴레오네는 갖가지 고민을 호소하는 사람들의 문제를 해결해주며 대부라 불리운다. 한편 솔로소라는 인물은 꼴레오네가와 라이벌인 탓타리아 패밀리와 손잡고 새로운 마약 사업을 제안한다. 돈 꼴레오네가 마약 사업에 참여하지 않기로 하자, 돈 꼴레오네를 저격해 그는 중상을 입고 사경을 헤매게 된다. 그 뒤, 돈 꼴레오네의 아들 소니는 조직력을 총 동원해 다른 패밀리들과 피를 부르는 전쟁을 시작하는데... 가족의 사업과 상관없이 대학에 진학한 뒤 인텔리로 지내왔던 막내 아들 마이클은 아버지가 총격을 당한 뒤, 아버지를 구하기 위해 위험천만한 협상 자리에 나선다.</p>
      <div style="display:flex">
        <a href="{% url 'movies:update' movie.pk %}" class="btn btn-primary">UPDATE</a>
        <form style="margin-left:10px;" action="{% url 'movies:delete' movie.pk %}">
          {% csrf_token %}
          <input type="submit" class="btn btn-danger"value="DELETE">
        </form>

      </div>
    </div>
  </div>
  <hr>
  <a href="{% url 'movies:index' %}" class="btn btn-warning">BACK</a>
{% endblock content %}
```
* 이 문제에서 어려웠던점 : 디테일하게 화면을 구성해야 하는 점이 어려웠습니다.
* 내가 생각하는 이 문제의 포인트 : 부트스트랩 카드로 화면 구성을 할 수 있는가


## D. create.html

* 요구 사항 :

“영화 생성 페이지”
• 특정 영화를 생성하기 위한 HTML form 요소를 표시합니다.
• 표시되는 form은 Movie 모델 클래스에 기반한 ModelForm이어야 합니다.
• 작성한 정보는 제출(submit)시 단일 영화 데이터를 저장하는 URL로 요청과 함께 전송됩니다.
• 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크를 표시합니다.

* 결과 :

  * 문제 접근 방법 및 코드 설명

```
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  <h1>CREATE</h1>
   <form action="{% url 'movies:create' %}" method='POST'>
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons %}
      <button type='submit' class='btn btn-primary'>Submit</button>
    {% endbuttons %}
   </form>
   <hr>
  <a href="{% url 'movies:index' %}" class="btn btn-primary">Back</a>
{% endblock content %}

```
* 이 문제에서 어려웠던점 : 모델폼 작성하는 것이 어려웠습니다.
* 내가 생각하는 이 문제의 포인트 : 데이터를 생성할 수 있는 페이지와 저장할 수 있는 DB를 구축하는 것.


## E. update.html

* 요구 사항 :
• “영화수정페이지”
  • 특정 영화를 수정하기 위한 HTML form 요소를 표시합니다.
  • 표시되는 form은 Movie 모델 클래스에 기반한 ModelForm이어야 합니다.
  • HTML input 요소에는 기존 데이터를 출력합니다.
  • Cancel 버튼은 사용자의 모든 입력을 초기값으로 재설정합니다.
  • 작성한 정보는 제출(submit) 시 단일 영화 데이터를 수정하는 URL로 요청과 함께 전송됩니다.
  • 영화 상세 정보페이지(detail.html)로 이동하는 링크를 표시합니다.
* 결과 :

  * 문제 접근 방법 및 코드 설명

```
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  <h1>UPDATE</h1>
   <form action="{% url 'movies:update' movie.pk %}" method='POST'>
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons %}
      <button type='submit' class='btn btn-primary'>Submit</button>
      <a class="btn btn-warning"href="{% url 'movies:update' movie.pk %}">
        Cancel
      </a>
      {% endbuttons %}
    </form>
   <hr>
  <a href="{% url 'movies:index' %}" class="btn btn-primary">Back</a>
{% endblock content %}

```
* 이 문제에서 어려웠던점 : 모델폼 작성하는 것이 어려웠습니다.
* 내가 생각하는 이 문제의 포인트 : DB에 저장한 정보를 수정하는 페이지를 구성하는 것.


# 후기

* pjt04에서 약간 응용하는 부분이 많았던 점은 수월하게 느껴졌으나, 모델폼 구축하는 것이 어려웠습니다.
* 역시 pjt는 쉬운 게 없는 것 같습니다.
