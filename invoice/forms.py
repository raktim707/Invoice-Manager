from django import forms
from django.forms import formset_factory
from phonenumber_field.formfields import PhoneNumberField
from .models import Invoice, Market

floor_numbers=[(i, str(i)) for i in range(1, 21)]
class InvoiceForm(forms.Form):
    
        # fields = ['customer', 'message']
    market = forms.ModelChoiceField(queryset=Market.objects.all(), label='market')
    floor = forms.TypedChoiceField(choices=floor_numbers, coerce=int)
    customer = forms.CharField(
        label='Cusomter',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Customer Name',
            'rows':1
        })
    )
    customer_phone =PhoneNumberField(
        label='Customer Phone',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'customer phone number',
            'rows':1
        })
    )
    total_amount = forms.DecimalField(label='Amount',widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Amount to be paid',
            'rows':1
        })
    )
    billing_address = forms.CharField(
        label='Billing Address',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'rows':1
        })
    )

class MarketForm(forms.Form):
    
    name = forms.CharField(
        label='Market',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Market Name'
        })
    )
    location = forms.CharField(
        label='Location',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Enter market address',
            "rows":1
        })
    )

class search_by_market_form(forms.ModelForm):
    class Meta:
        model =Market
        fields = ('name',)

    # amount = forms.DecimalField(
    #     disabled = True,
    #     label='Amount $',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control input',
    #     })
    # )
    
#LineItemFormset = formset_factory(LineItemForm, extra=1)