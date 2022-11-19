from django.shortcuts import render
from .models import  CatchReceipt, Invoices

def dashboard_financial(request):
    catch_teceipt = CatchReceipt.objects.all()
    invoices = Invoices.objects.all()


    total_catch = catch_teceipt.count()
    total_invoices = invoices.count()


    # invoices_raised = invoices.filter().count()
    billed_bonds = catch_teceipt.filter(invoices_id=None).count()
    
    
    context = {
        'total_catch':total_catch,
        'total_invoices':total_invoices,
        'billed_bonds':billed_bonds,
    }
    return render(request, 'financial/dashbaord.html', context)



