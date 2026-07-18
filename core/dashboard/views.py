from django.shortcuts import render

# Create your views here.

def welcome_page(request):
    return render(request,'dashboard/index.html',{"name":"Nila"})