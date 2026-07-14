from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:product_id>/',views.int_item,name='product-int'),
    path('<str:product_id>/',views.text_item),
]
