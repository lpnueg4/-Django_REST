# from django.conf.urls import url
# from snippets import views
# from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

# ------------

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views_3

urlpatterns = [
    url(r'^snippets/$', views_3.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views_3.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)