from django.conf.urls import patterns
from django.conf.urls import url

from views import AuthorCreate, AuthorUpdate, AuthorDelete

from views import OrderDetailView
from views import OrderResultsView

urlpatterns = patterns('',
    url(
      regex=r'^(?P<pk>\d+)/$',
      view=OrderDetailView.as_view(),
      name='detail'
    ),
    url(
      regex=r'^?P<pk>\d+)/results/$',
      view=OrderResultsView.as_view(),
      name='results'
    ),
    url(r'author/add/$', AuthorCreate.as_view(), name='author_add'),
    url(r'author/(?P<pk>\d+)/$', AuthorUpdate.as_view(), name='author_update'),
    url(r'author/(?P<pk>\d+)/delete/$', AuthorDelete.as_view(), name='author_delete'),
)