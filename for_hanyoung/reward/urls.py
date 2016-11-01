from django.conf.urls import url

from reward import views

urlpatterns = [
    url(r'^main/$', views.reward_main, name='reward_main'),
    url(r'^detail/$', views.reward_detail, name='reward_detail'),
    url(r'^add/$', views.reward_add, name='reward_add'),

]
