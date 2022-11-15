from random import choices
from django.db import models

# Create your models here.


class DriverModel(models.Model):
    driver_id = models.BigAutoField(primary_key=True)
    driver_name = models.CharField(max_length=225,  help_text='اسم السائق')
    Saudi_Arabia = 'Saudi'
    YEMEN = 'Yemeni'
    Syria = 'Syrian'
    Egypt = 'Egypt'
    Afghanistan = 'Afghanistan'
    Pakistan = 'Pakistani'
    Jordan = 'Jordanian'
    India = 'Indian'
    Other = 'other'
    countrys = [
        (Saudi_Arabia, 'Saudi'),
        (YEMEN, 'Yemeni'),
        (Syria, 'Syrian'),
        (Egypt, 'Egypt'),
        (Afghanistan, 'Afghanistan'),
        (Pakistan, 'Pakistani'),
        (Jordan, 'Jordanian'),
        (India, 'Indian'),
        (Other, 'other')
    ]
    driver_nationality = models.CharField(
        max_length=20, choices=countrys, default=Other,  help_text='جنسية السائق')
    driver_phone_number = models.CharField(
        max_length=16, help_text='رقم هاتف السائق ')
    Identification_Number = models.CharField(
        max_length=10,  help_text='رقم الهوية/الاقامة')
    truck_plate_number = models.CharField(
        max_length=8,  help_text='رقم لوحة الشاحنة')
    Truck_Reefers = 'Truck_Reefers'
    Truck_Flatbed  = 'Truck_Flatbed'
    Truck_high_sides = 'Truck_high_sides'
    Truck_Curtainsider = 'Truck_Curtainsider'
    lory_Flatbed= 'lory_Flatbed'
    lory_Reefers= 'lory_Reefers'
    dinah_Flatbed= 'dinah_Flatbed'
    dinah_Reefers= 'dinah_Reefers'
    
   
    Vehicle = [
        (Truck_Reefers, 'Truck_Reefers'),
        (Truck_Flatbed, 'Truck_Flatbed'),
        (Truck_high_sides, 'Truck_high_sides'),
        (Truck_Curtainsider, 'Truck_Curtainsider'),
        (lory_Flatbed, 'lory_Flatbed'),
        (lory_Reefers, 'lory_Reefers'),
        (dinah_Flatbed, 'dinah_Flatbed'),
        (dinah_Reefers, 'dinah_Reefers'),
    ]
    Vehicle_Type = models.CharField( choices=Vehicle, default=Truck_Flatbed,
        max_length=30, help_text='نوع السيارة(سطحة - جوانب) ....')
    Sequence_Number = models.CharField(
        max_length=30, help_text='الرقم التسلسلي من الاستمارة')
    Owner_car_id_number = models.CharField(
        max_length=10,  help_text='رقم هوية مالك السيارة')
    Identification_photo = models.ImageField(
        upload_to='driver/', null=True, help_text='صورة الهوية/الاقامة ')
    # license_photo = models.ImageField(upload_to='driver/', null=True, help_text=' صورة رخصة القيادة')
    # Sequence_image = models.ImageField(upload_to='driver/', null=True, help_text=' صورة من استمارة السيارة')
    # car_picture = models.ImageField(upload_to='driver/', null=True, help_text=' صورة جانبية او امامية للسيارة')

    def __str__(self):
        return self.driver_name
