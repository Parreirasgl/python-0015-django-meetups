from django.shortcuts import render

def index(request): 
    lista = [1, 2, 3, 4]
    return render(request, 'meetups/index.html', {'var1': lista})


