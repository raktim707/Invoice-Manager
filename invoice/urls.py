from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import InvoiceListView, createInvoice, generate_PDF, view_PDF, create_market, EditInvoice, list_by_market, DeleteInvoice, paid_invoice_list, due_invoice_list

app_name = 'invoice'
urlpatterns = [
    path('', login_required(InvoiceListView.as_view()), name="invoice-list"),
    path('paid_invoices/', paid_invoice_list, name="paid-invoices"),
    path('due-invoices/', due_invoice_list, name='due-invoices'),
    path('create/', createInvoice, name="invoice-create"),
    path('<int:id>/byMarket', list_by_market, name="list_by_market"),
    path('invoice-detail/<id>', view_PDF, name='invoice-detail'),
    path('invoice-download/<id>', generate_PDF, name='invoice-download'),
    path('create-market/', create_market, name='create-market'),
    path('edit-invoice/<int:pk>', EditInvoice.as_view(), name='edit-invoice'),
    path('delete-invoice/<int:pk>', DeleteInvoice.as_view(), name='delete-invoice')
]
