from django.urls import path
from .views import AboutViews
from . import views

urlpatterns = [
    path("",AboutViews.as_view(),name='about')
]
