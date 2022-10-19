from django.shortcuts import render

def home(request):
    movie = ['reflection on you', 'harry potter', 'spider man',]
    
    context = {
        'movie' : movie,
    }
    
    return render(request, 'movies/home.html', context)
