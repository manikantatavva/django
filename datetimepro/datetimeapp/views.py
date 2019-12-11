from django.shortcuts import render
from django.http.response import HttpResponse
import datetime
date1=datetime.datetime.now()
def dt(request):
    x='today date and time is{}',format(date1)
    return HttpResponse(x)