__author__ = 'egslava'


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'(?P<source>.+?)/(?P<target>.+?)/(?P<text>.+?)/', views.index, name="index")
    # url('source=(?P<text>[\w+])/source=(?P<source>[\w+]))/target=(?P<target>[.*?])&', views.index, name='index'),
]
