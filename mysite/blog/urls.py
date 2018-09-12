from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', post_model_list_view, name='list'),
    url(r'^create/$', post_model_create_view, name='create'),
    url(r'^(?P<id>\d+)/$', post_model_detail_view, name='detail'),
    url(r'^(?P<id>\d+)/update/$', post_model_update_view, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_model_delete_view, name='delete'),
]