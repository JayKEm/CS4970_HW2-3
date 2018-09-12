from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, include

from blog.views import post_model_list_view

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    url(r'^blog/',include(('blog.urls','blog'),namespace='blog')),
]