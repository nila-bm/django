from django.shortcuts import render

# Create your views here.
lst=["nila","reza","nika"]

def welcome_page(request):
    return render(request,'dashboard/index.html',{"names":lst})