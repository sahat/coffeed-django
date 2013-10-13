from django import forms

class OrderForm(forms.Form):
    name = forms.CharField()
    order_number = forms.IntegerField()

    def send_email(self):
        pass
