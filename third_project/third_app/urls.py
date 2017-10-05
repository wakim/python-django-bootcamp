from django.conf.urls import url
from third_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form_page', views.form_name_view, name='form_name_view')
]
