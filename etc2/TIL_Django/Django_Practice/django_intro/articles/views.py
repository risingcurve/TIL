from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def greeting(request):
    return render(request, 'greeing.html', {'name': 'Alice'})

