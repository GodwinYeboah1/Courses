from django.conf.urls import url

from .  import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/destory/(?P<id>\d+)$', views.destory),
    url(r'^courses/new$', views.create)
]
