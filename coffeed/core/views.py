from django.views.generic import DetailView
from models import Item, Order


class OrderDetailView(DetailView):
    model = Order


class OrderResultsView(OrderDetailView):
    template_name = 'core/results.html'