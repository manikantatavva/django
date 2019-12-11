from django.conf.urls import include,url
from django.contrib import admin
from maniapp import views

urlpatterns = [
    url(r'^admin/',include( admin.site.urls)),
    url(r'^home/',views.home),
    url(r'^name/',views.name),
    url(r'^contact/',views.contact),
    url(r'^$',views.contact)
]
