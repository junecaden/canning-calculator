from django.conf.urls import url

from . import views

app_name = 'calc'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<test>[0-9]+)/result/$', views.result, name='result'),
    
    # ex: /polls/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/result/$', views.vote, name='result'),
]
