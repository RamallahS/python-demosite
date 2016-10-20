from django.conf.urls import url

from openapi import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
