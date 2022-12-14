# Generated by Django 4.1.2 on 2022-11-22 14:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('drivers', '0002_remove_drivermodel_identification_photo'),
        ('financial', '0010_remove_invoices_auth_invoices_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='catchreceipt',
            name='Vehicle_Type',
            field=models.CharField(blank=True, choices=[('تريلا براد', 'تريلا براد'), ('سطحة', 'سطحة'), ('جوانب عالي', 'جوانب عالي'), ('ستارة', 'ستارة'), ('لوري عادي', 'لوري عادي'), ('لوري براد', 'يدنة عادي'), ('يدنة عادي', 'يدنة عادي'), ('دينة براد', 'دينة براد')], default='سطحة', help_text='نوع السيارة(سطحة - جوانب) ....', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='catchreceipt',
            name='Shipment_id',
            field=models.CharField(blank=True, default='', help_text=' رقم الشحن', max_length=225),
        ),
        migrations.AlterField(
            model_name='catchreceipt',
            name='amount',
            field=models.CharField(blank=True, help_text=' الاجرة', max_length=225),
        ),
        migrations.AlterField(
            model_name='catchreceipt',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.companymodel'),
        ),
        migrations.AlterField(
            model_name='catchreceipt',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text=' التاريخ'),
        ),
        migrations.AlterField(
            model_name='catchreceipt',
            name='deduction',
            field=models.CharField(blank=True, help_text='خصم', max_length=225),
        ),
        migrations.AlterField(
            model_name='catchreceipt',
            name='destination',
            field=models.CharField(blank=True, default='الرياض', help_text=' الوجهة', max_length=225),
        ),
        migrations.AlterField(
            model_name='catchreceipt',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drivers.drivermodel'),
        ),
        migrations.AlterField(
            model_name='catchreceipt',
            name='notice_number',
            field=models.CharField(blank=True, default='', help_text=' رقم الاشعار', max_length=225),
        ),
        migrations.AlterField(
            model_name='catchreceipt',
            name='overnight',
            field=models.CharField(blank=True, help_text=' المبات', max_length=225),
        ),
        migrations.AlterField(
            model_name='catchreceipt',
            name='policy_number',
            field=models.CharField(blank=True, default='', help_text=' رقم البوليصة', max_length=225),
        ),
        migrations.AlterField(
            model_name='catchreceipt',
            name='return_fare',
            field=models.CharField(blank=True, help_text=' اجرة رجعة', max_length=225),
        ),
        migrations.AlterField(
            model_name='catchreceipt',
            name='source',
            field=models.CharField(blank=True, default='جدة', help_text=' المصدر', max_length=225),
        ),
    ]
