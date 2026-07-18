from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
# Create your views here.

int_dict={
1:"PS5",
2:"PS4",
3:"Xbox",
}
text_dict={
    "1st":1,
    "2st":2,
    "3st":3
}
def index(request):
    return HttpResponse ('welcome to the product')

def int_item(request,product_id):
    if product_id in int_dict:
        return HttpResponse(int_dict[product_id])
    else:
        return HttpResponseNotFound ("product Not Found")
    
def text_item (request,product_id):
    if product_id in text_dict:
        return HttpResponseRedirect(reversed('product-int',args=[text_dict[product_id]]))
    else :
        return HttpResponseNotFound ("product Not Found")
    