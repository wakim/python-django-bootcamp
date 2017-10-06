from django.conf.urls import url
from fourth_app import views

app_name = 'fourth_app'
urlpatterns = [
    url(r'^other/$', views.other, name='other'),
    url(r'^relative/$', views.relative, name='relative'),
]
