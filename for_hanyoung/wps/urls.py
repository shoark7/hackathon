from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^$', views.wps_index, name='wps_index'),
    url('^wps/list/$', views.wps_list, name='wps_list'),
    url('^wps/detail/(?P<student_id>\d+)/$', views.wps_detail, name='wps_detail'),
]