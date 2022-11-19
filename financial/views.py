from django.shortcuts import render, redirect, get_object_or_404

from .models import  CatchReceipt, Invoices
from .forms import AddCatch


def dashbaord(request):
    return render(request, 'financial/dashbaord.html')



def all_catch_receipt_list(request):
    catch_receipt = CatchReceipt.objects.all()
    return render(request, 'financial/catch/catch_receipt_list.html',{'catch_receipt':catch_receipt})





def catch_receipt_list(request, status):
    if status == 'all':
        catch_receipt = CatchReceipt.objects.all()
    else:
        catch_receipt  = CatchReceipt.objects.filter(invoices_id = None )

    return render(request, 'financial/catch/catch_receipt_list.html',{'catch_receipt':catch_receipt})


def catch_receipt_details(request, pk):
    catch_receipt = get_object_or_404(CatchReceipt, pk=pk)
    return render(request, 'financial/catch/catch_receipt_details.html',{'catch_receipt':catch_receipt})

def add_catch_receipt(request):
    if request.method == 'POST':
        catch_receipt_form = AddCatch(request.POST, request.FILES)
        if catch_receipt_form.is_valid():
            catch_receipt_form.save()
            return redirect('all_catch_receipt_list')
    else:
        catch_receipt_form = AddCatch()

    return render(request, 'financial/catch/catch_receipt_add_edit.html',{'catch_receipt_form':catch_receipt_form})


def edit_catch_receipt(request, pk):
    catch_receipt = get_object_or_404(CatchReceipt, pk=pk)
    if request.method == 'POST':
        catch_receipt_form = AddCatch(request.POST, instance=catch_receipt)
        if catch_receipt_form.is_valid():
            catch_receipt_form.save()
            return redirect('all_catch_receipt_list')
    else:
        catch_receipt_form = AddCatch(instance=catch_receipt)

    return render(request, 'financial/catch/catch_receipt_add_edit.html',{'catch_receipt_form':catch_receipt_form})

def delete_catch_receipt(request, pk):
    catch_receipt = get_object_or_404(CatchReceipt, pk=pk)
    catch_receipt.delete()
    return redirect('all_catch_receipt_list')