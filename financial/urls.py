from django.urls import path
from . import views


urlpatterns = [
    path('financial/',views.catch_receipt_list, name='catch_receipt_list' ),
    path('financial/details/<int:pk>',views.catch_receipt_details, name='catch_receipt_details' ),
    path('financial/add',views.add_catch_receipt, name='add_catch_receipt' ),
    path('financial/edit/<int:pk>',views.edit_catch_receipt, name='edit_catch_receipt' ),
    path('financial/delete/<int:pk>',views.delete_catch_receipt, name='delete_catch_receipt' ),
]
