from django.contrib import admin

from .models import Invoice, Market

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date', 'due_date', 'total_amount', 'customer_phone']
    list_filter=['market',]
    search_fields = ['customer', 'market']
admin.site.register(Market)
# Register your models here.
