from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
dictionary={"google":"https://google.com",
            "apple":"https://apple.com",
            "yahoo":"https://yahoo.com",}

def index(request):
    return render(request, 'dashboard/index.html', {
        'content': 'Welcome to the Home Page'
    })

def welcome_page(request):
    return render(request,'dashboard/index.html',{"links":dictionary})