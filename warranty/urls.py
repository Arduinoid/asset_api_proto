from django.conf.urls import url
from warranty import views


urlpatterns = [
    url(r'^servers/$', views.server_list),
    url(r'^servers/(?P<pk>[0-9]+)/$', views.server_detail)
]