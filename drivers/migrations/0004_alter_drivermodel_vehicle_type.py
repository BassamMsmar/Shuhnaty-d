# Generated by Django 4.1.2 on 2022-11-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0003_alter_drivermodel_identification_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivermodel',
            name='Vehicle_Type',
            field=models.CharField(blank=True, choices=[('تريلا براد', 'تريلا براد'), ('سطحة', 'سطحة'), ('جوانب عالي', 'جوانب عالي'), ('ستارة', 'ستارة'), ('لوري عادي', 'لوري عادي'), ('لوري براد', 'يدنة عادي'), ('يدنة عادي', 'يدنة عادي'), ('دينة براد', 'دينة براد')], default='سطحة', help_text='نوع السيارة(سطحة - جوانب) ....', max_length=30, null=True),
        ),
    ]
