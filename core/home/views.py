from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class AboutViews(TemplateView):
    template_name="home/about.html"