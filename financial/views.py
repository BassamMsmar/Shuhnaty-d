from django.shortcuts import render, redirect, get_object_or_404

from .models import  CatchReceipt
from .models import  Invoices


# financial
#catch_receipt
# financials
# Create your views here.
def catch_receipt_list(request):
    catch_receipt = CatchReceipt.objects.all()
    return render(request, 'financial/catch_receipt_list.html',{'catch_receipt':catch_receipt})

def catch_receipt_details(request, pk):
    catch_receipt = get_object_or_404(CatchReceipt, pk=pk)
    return render(request, 'financial/catch_receipt_details.html',{'catch_receipt':catch_receipt})

def add_catch_receipt(request):
    if request.method == 'POST':
        catch_receipt_form = CatchReceipt(request.POST, request.FILES)
        if catch_receipt_form.is_valid():
            catch_receipt_form.save()
            return redirect('catch_receipt_list')
    else:
        catch_receipt_form = CatchReceipt()

    return render(request, 'financial/catch_receipt_add_edit.html',{'catch_receipt_form':catch_receipt_form})


def edit_catch_receipt(request, pk):
    catch_receipt = get_object_or_404(CatchReceipt, pk=pk)
    if request.method == 'POST':
        catch_receipt_form = CatchReceipt(request.POST, instance=catch_receipt)
        if catch_receipt_form.is_valid():
            catch_receipt_form.save()
            return redirect('catch_receipt_list')
    else:
        catch_receipt_form = CatchReceipt(instance=catch_receipt)

    return render(request, 'financial/catch_receipt_add_edit.html',{'catch_receipt_form':catch_receipt_form})

def delete_catch_receipt(request, pk):
    catch_receipt = get_object_or_404(CatchReceipt, pk=pk)
    catch_receipt.delete()
    return redirect('catch_receipt_list')