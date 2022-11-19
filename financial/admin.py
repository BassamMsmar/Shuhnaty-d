from django.contrib import admin

# Register your models here.
from .models import CatchReceipt, Invoices




admin.site.register( Invoices)
admin.site.register(CatchReceipt)