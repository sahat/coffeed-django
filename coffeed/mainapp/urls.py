from django.conf.urls import patterns
from django.conf.urls import url

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
)