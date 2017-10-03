from django.conf.urls import url
from second_app import views

urlpatterns = [
    url(r'^help/$', views.help, name='help'),
    url(r'^$', views.index, name='index'),
]
