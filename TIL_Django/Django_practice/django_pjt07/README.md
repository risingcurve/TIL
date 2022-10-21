# PJT 07

### 이번 pjt 를 통해 배운 내용

* REST API 설계

## 0. 공통 요구사항

* 요구 사항 :
• 모델 간의 관계 설정 후, 다음과 같은 기능을 구현합니다
A. Actor
  i. 배우 데이터 조회
B. Movie
  i. 영화 데이터 조회
C. Review
  i. 리뷰 데이터 조회 / 생성 / 수정 / 삭제


  * 문제 접근 방법 및 코드 설명 : 서로 참조하는 로직을 최대한 이해해 보면서 접근하려 했고, 어려운 부분은 교재를 참고했습니다.

```
# models.py

from platform import release
from pyexpat import model
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='movies')

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
```

```

# urls.py

from django.urls import path
from . import views


urlpatterns = [
    path("actors/", views.actor_list),
    path("actors/<int:actor_pk>/", views.actor_detail),
    path("movies/", views.movie_list),
    path("movies/<int:movie_pk>/", views.movie_detail),
    path("reviews/", views.review_list),
    path("reviews/<int:review_pk>/", views.review_detail),
]
```


```
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Actor, Movie, Review
from .serializers import ActorListSerializer, ActorSerializer, MovieListSerializer, MovieSerializer , ReviewListSerializer, ReviewSerializer
from rest_framework import status


@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all( )
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all( )
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all( )
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

```

```
from dataclasses import field
from rest_framework import serializers
from .models import Movie, Actor, Review


class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = ('id', 'name')


class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieTitleSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'
        

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title', 'overview',)


class ActorNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)


class MovieTitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title',)
        read_only_fields = ('actors',)
        


class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('title', 'content',)


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorNameSerializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'




class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

```


* 이 문제에서 어려웠던점 : 각각의 Detail에서 'movies - title', 'actors - name', 'movies - title'을 뽑아낼 수 있도록 serialize하는 것.
* 내가 생각하는 이 문제의 포인트 : 
 - actors = models.ManyToManyField(Actor, related_name='movies')를 통해 M:N 관계를 설정하는 것.






# 후기

* 로직이 진짜 복잡한 것 같습니다. 코드 길이는 그렇게 길지 않음에도 불구하고, 복잡한 로직을 요구한다는 점에서 굉장히 훌륭한 문제 같습니다.
* 역시 pjt는 쉬운 게 없는 것 같습니다.
