from django.conf.urls import include, url
from django.contrib import admin
from fakerapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^data/',views.fake_view),
    url(r'^$',views.fetching_data)
]
