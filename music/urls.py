
from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'music'

urlpatterns = [



   # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #music/712
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),

]
