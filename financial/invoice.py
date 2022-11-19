from django.shortcuts import render, redirect, get_object_or_404

from .models import Invoices
from .models import  CatchReceipt
from .forms import AddInvoices


def invoice_list(request):
    invoice = Invoices.objects.all()
    # total_invoice = invoice.CatchReceipt().count()
    return render(request, 'financial/invoice/invoice_list.html',{
        'invoice':invoice,
        # 'total_invoice':total_invoice,
        })

def invoice_details(request, pk):
    invoice = get_object_or_404(Invoices, pk=pk)
    catchs = CatchReceipt.objects.filter(invoices=invoice)
    return render(request, 'financial/invoice/invoice_details.html',{
        'invoice':invoice,
        'catchs':catchs,
        })

def add_invoice(request):
    if request.method == 'POST':
        invoice_form = AddInvoices(request.POST, request.FILES)
        if invoice_form.is_valid():
            invoice_form.save()
            return redirect('invoice_list')
    else:
        invoice_form = AddInvoices()

    return render(request, 'financial/invoice/invoice_add_edit.html',{'invoice_form':invoice_form})


def edit_invoicet(request, pk):
    invoice = get_object_or_404(invoice, pk=pk)
    if request.method == 'POST':
        invoice_form = AddInvoices(request.POST, instance=Invoices)
        if invoice_form.is_valid():
            invoice_form.save()
            return redirect('invoice_list')
    else:
        invoice_form = AddInvoices(instance=invoice)

    return render(request, 'financial/invoice/invoice_add_edit.html',{'invoice_form':invoice_form})

def delete_invoice(request, pk):
    invoice = get_object_or_404(Invoices, pk=pk)
    invoice.delete()
    return redirect('invoice_list')