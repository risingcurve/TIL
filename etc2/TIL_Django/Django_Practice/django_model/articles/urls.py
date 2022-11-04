from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('catchword/<name>/', views.catchword, name="catchword"),
]

# 2가지 지원해줍니다.
# 1. string (default)
#             <str:str1>
# 2. integer <int:num1>