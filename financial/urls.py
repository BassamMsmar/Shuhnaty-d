from django.urls import path
from . import views, invoice
from . import utils


urlpatterns = [
    path('financial/dashbaord/',utils.dashboard_financial, name='dashboard_financial' ),
    path('financial/catch/',views.catch_receipt_list, name='catch_receipt_list' ),
    path('financial/catch/details/<int:pk>',views.catch_receipt_details, name='catch_receipt_details' ),
    path('financial/catch/add/',views.add_catch_receipt, name='add_catch_receipt' ),
    path('financial/catch/edit/<int:pk>',views.edit_catch_receipt, name='edit_catch_receipt' ),
    path('financial/catch/delete/<int:pk>',views.delete_catch_receipt, name='delete_catch_receipt' ),


    path('financia/invoice/',invoice.invoice_list, name='invoice_list' ),
    path('financia/invoice/details/<int:pk>',invoice.invoice_details, name='invoice_details' ),
    path('financia/invoice/add',invoice.add_invoice, name='add_invoice' ),
    path('financia/invoice/edit/<int:pk>',invoice.edit_invoicet, name='edit_invoicet' ),
    path('invoice/invoice/lete/<int:pk>',invoice.delete_invoice, name='delete_invoice' ),




]
