from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.partners, name='partners'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^edit/done/$', views.add, name='done'),
]