from django.db import models
from django.utils import timezone

from accounts.forms import User
from companies.models import CompanyModel
from drivers.models import DriverModel

# Create your models here.
class CatchReceipt(models.Model):
    catchReceipt_id= models.BigAutoField(primary_key=True)
    driver = models.ForeignKey(DriverModel, on_delete=models.CASCADE, null=True)
    source =  models.CharField(max_length=225,  default='' , help_text=' المصدر')
    destination =  models.CharField(max_length=225,  help_text=' الوجهة')
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now)
    amount =  models.CharField(max_length=225,  help_text=' الاجرة')
    overnight =  models.CharField(max_length=225,  help_text=' المبات')
    return_fare =  models.CharField(max_length=225,  help_text=' اجرة رجعة')
    deduction =  models.CharField(max_length=225,  help_text='خصم')
    policy_number =  models.CharField(max_length=225,  default='' , help_text=' رقم البوليصة')
    notice_number =  models.CharField(max_length=225,  default='' , help_text=' رقم الاشعار')
    Shipment_id =  models.CharField(max_length=225,  default='' , help_text=' رقم الشحن')
    delegate =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    accountant =  models.CharField(max_length=225, null=True)


class Invoices(models.Model):
    invoices_id= models.BigAutoField(primary_key=True)
    CatchReceipt= models.ManyToManyField(CatchReceipt)
    date = models.DateTimeField(default=timezone.now)
    auth =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  