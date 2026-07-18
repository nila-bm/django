from django.shortcuts import render

# Create your views here.
dictionary={"google":"https://google.com",
            "apple":"https://apple.com",
            "yahoo":"https://yahoo.com",}

def welcome_page(request):
    return render(request,'dashboard/index.html',{"links":dictionary})