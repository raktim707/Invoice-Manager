from django.contrib import admin
from django.urls import path
from .views import InvoiceListView, createInvoice, generate_PDF, view_PDF, create_market, EditInvoice

app_name = 'invoice'
urlpatterns = [
    path('', InvoiceListView.as_view(), name="invoice-list"),
    path('create/', createInvoice, name="invoice-create"),
    path('invoice-detail/<id>', view_PDF, name='invoice-detail'),
    path('invoice-download/<id>', generate_PDF, name='invoice-download'),
    path('create-market/', create_market, name='create-market'),
    path('edit-invoice/<int:pk>', EditInvoice.as_view(), name='edit-invoice')
]
