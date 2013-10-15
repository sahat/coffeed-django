from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import TemplateView

from views import OrderDetailView
from views import OrderResultsView
from views import OrderCreateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    url(
      regex=r'^order/$',
      view=OrderCreateView.as_view(),
      name='order'
    ),
    #url(
    #  regex=r'^(?P<pk>\d+)/$',
    #  view=OrderDetailView.as_view(),
    #  name='detail'
    #),
    #url(
    #  regex=r'^?P<pk>\d+)/results/$',
    #  view=OrderResultsView.as_view(),
    #  name='results'
    #),
)