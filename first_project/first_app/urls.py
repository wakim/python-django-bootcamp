from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users', views.users, name='users'),
    url(r'^signup', views.signup, name='signup')
]
