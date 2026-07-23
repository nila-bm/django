from django.urls import path
from . import views

urlpatterns = [
    path("",views.AboutViews.as_view(),name='about')
]
