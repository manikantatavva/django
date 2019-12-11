from django.shortcuts import render
from django.http.response import HttpResponse

def home(request):
    x="<h1>welcome to maniapp</h1>"
    return HttpResponse(x)
def name(request):wq
    y='manikanta'
    return HttpResponse(y)
def contact(request):
    z='my no is 0123456789'
    return HttpResponse(z)

