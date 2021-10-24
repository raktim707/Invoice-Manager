from django.db import models
import datetime
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Market(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)

class Invoice(models.Model):
    customer = models.CharField(max_length=100)
    customer_phone = PhoneNumberField(null=True, blank=True)
    billing_address = models.CharField(max_length=250,null=True, blank=True)
    floor = models.IntegerField(null=True)
    date = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    status = models.BooleanField(default=False)
    market = models.ForeignKey(Market, on_delete=models.CASCADE, null=True)
    class Meta:
        ordering = ('due_date',)
    def __str__(self):
        return str(self.customer)
    
    def get_status(self):
        return self.status

    # def save(self, *args, **kwargs):
        # if not self.id:             
        #     self.due_date = datetime.datetime.now()+ datetime.timedelta(days=15)
        # return super(Invoice, self).save(*args, **kwargs)

