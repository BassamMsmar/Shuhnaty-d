# Generated by Django 4.1.3 on 2022-11-14 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drivers', '0001_initial'),
        ('financial', '0002_remove_invoices_accountant_catchreceipt_accountant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catchreceipt',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.companymodel'),
        ),
        migrations.AlterField(
            model_name='catchreceipt',
            name='delegate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='catchreceipt',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='drivers.drivermodel'),
        ),
    ]
