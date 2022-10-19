from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('home/', views.home, name='home'),
]

# movies/home/
# articles/