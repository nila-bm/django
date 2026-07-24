from django.shortcuts import render
from .models import Farm

# Create your views here.

def farm(request):
    farms=Farm.objects.all()
    return render(request,'farm/index.html',{'farms':farms})