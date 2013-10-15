from django.views.generic import DetailView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin

from models import Item, Order
from forms import OrderForm


class OrderDetailView(LoginRequiredMixin, FormView):
    form_class = OrderForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super(OrderDetailView, self).form_valid(form)


class OrderResultsView(ListView):
    template_name = 'core/item_list.html'


class OrderCreateView(CreateView):
    model = Order

    def form_valid(self, form):
        # Custom logic goes here
        return super(OrderCreateView, self).form_valid(form)

    def form_invalid(self, form):
        # Custom Logic goes here
        return super(OrderCreateView, self).form_invalid(form)


class OrderUpdate(UpdateView):
    model = Order


#class OrderDelete(DeleteView):
#    model = Author
#    success_url = reverse_lazy('author-list')