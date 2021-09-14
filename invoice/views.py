from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic.edit import DeleteView, UpdateView
from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View
from .models import Invoice, Market
from .forms import InvoiceForm, MarketForm

import pdfkit

class InvoiceListView(View):
    def get(self, *args, **kwargs):
        invoices = Invoice.objects.all()
        context = {
            "invoices":invoices,
        }

        return render(self.request, 'invoice/invoice-list.html', context)
    
    def post(self, request):        
        # import pdb;pdb.set_trace()
        invoice_ids = request.POST.getlist("invoice_id")
        invoice_ids = list(map(int, invoice_ids))

        update_status_for_invoices = int(request.POST['status'])
        invoices = Invoice.objects.filter(id__in=invoice_ids)
        # import pdb;pdb.set_trace()
        if update_status_for_invoices == 0:
            invoices.update(status=False)
        else:
            invoices.update(status=True)

        return redirect('invoice:invoice-list')

def createInvoice(request):
    """
    Invoice Generator page it will have Functionality to create new invoices, 
    this will be protected view, only admin has the authority to read and make
    changes here.
    """

    heading_message = 'Formset Demo'
    if request.method == 'GET':
        form = InvoiceForm(request.GET or None)
    elif request.method == 'POST':
        form = InvoiceForm(request.POST)
        
        if form.is_valid():
            m = form.data["market"]
            print("message: ", m)
            market = get_object_or_404(Market, id=m)
            print(market)
            invoice = Invoice.objects.create(market=market, customer=form.data["customer"],
                    customer_phone=form.data["customer_phone"],
                    total_amount=form.data['total_amount'],
                    billing_address = form.data["billing_address"],
                    date=form.data["date"],
                    due_date=form.data["due_date"], 
                    )
            
            try:
                generate_PDF(request, id=invoice.id)
            except Exception as e:
                print(f"********{e}********")
            return redirect('/')
    context = {
        "title" : "Invoice Generator",
        "form": form,
    }
    return render(request, 'invoice/invoice-create.html', context)

class EditInvoice(UpdateView):
    model = Invoice
    fields = '__all__'
    template_name = 'invoice/edit_invoice.html'



def create_market(request):
    if request.method == 'GET':
        form = MarketForm(request.GET or None)
    elif request.method == 'POST':
        form = MarketForm(request.POST)
    if form.is_valid():
        market = Market.objects.create(name=form.data['name'], location=form.data['location'])
        return redirect('/')
    return render(request, 'invoice/market-create.html', {'form': form})


def view_PDF(request, id=None):
    invoice = get_object_or_404(Invoice, id=id)
    

    context = {
        "company": {
            "name": "Ibrahim Services",
            "address" :"67542 Jeru, Chatsworth, CA 92145, US",
            "phone": "(818) XXX XXXX",
            "email": "contact@ibrahimservice.com",
        },
        "invoice_id": invoice.id,
        "invoice_total": invoice.total_amount,
        "customer": invoice.customer,
        "customer_phone": invoice.customer_phone,
        "date": invoice.date,
        "due_date": invoice.due_date,
        "billing_address": invoice.billing_address,
        "market": invoice.market,

    }
    return render(request, 'invoice/pdf_template.html', context)

def generate_PDF(request, id):
    # Use False instead of output path to save pdf to a variable
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('invoice:invoice-detail', args=[id])), False)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    return response


def change_status(request):
    return redirect('invoice:invoice-list')

def view_404(request,  *args, **kwargs):

    return redirect('invoice:invoice-list')