# coding:u8

from django.conf.urls import url

from g1 import views

urlpatterns = [
    url(r'^other/test1$', views.other1, name='test1'),
    url(r'^other/test2/(?P<name>.*)/$', views.other2, name='test2'),
    url(r'^other/test3/(?P<n1>\d+),(?P<n2>\d+)/$', views.other3, name='test3'),
    url(r'^other/test4$', views.other4.as_view(), name='test4'),

    url(r'^VM/vm1$', views.vm1, name='vm1'),
    url(r'^VM/vm2$', views.vm2, name='vm2'),
    url(r'^VM/vm3$', views.vm3, name='vm3'),
    url(r'^VM/vm4$', views.vm4, name='vm4'),
    url(r'^VM/vm5$', views.vm5, name='vm5'),

    url(r'^test/schema$', views.schema_view, name='schema_view'),
]