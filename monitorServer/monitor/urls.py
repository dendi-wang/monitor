#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^test/', views.test),
    url(r'^$', views.index),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^triggers/$', views.triggers, name='triggers'),
    url(r'hosts/$', views.hosts, name='hosts'),
    url(r'hosts/(\d+)/$', views.host_detail, name='host_detail'),
    url(r'trigger_list/$', views.trigger_list, name='trigger_list'),

]
