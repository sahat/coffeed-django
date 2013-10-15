from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import TemplateView

from views import OrderCreateView

urlpatterns = patterns('',
    url(r'^sell/$', OrderCreateView.as_view(), name='sell_order'),
    url(r'^sell/new/$', OrderCreateView.as_view(), name='sell_order'),
)