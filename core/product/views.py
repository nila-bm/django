from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.

_dict={
"001":"PS5",
"002":"PS4",
"003":"Xbox",
}
def index(request):
    return HttpResponse ('welcome to the product')

def item(request,product_id):
    if product_id in _dict:
        return HttpResponse(_dict[product_id])
    else:
        return HttpResponseNotFound ("product Not Found")