from django.shortcuts import render, redirect, get_object_or_404
from num2words import num2words

from .models import  CatchReceipt
from .forms import AddCatch
from .filters import CatchFielter


def dashbaord(request):
    return render(request, 'financial/dashbaord.html')



def catch_receipt_list(request):
    catch_receipt = CatchReceipt.objects.all()
    myFilter = CatchFielter(request.GET, queryset=catch_receipt)
    catch_receipt = myFilter.qs


    return render(request, 'financial/catch/catch_receipt_list.html',{
        'catch_receipt':catch_receipt,
        'myFilter':myFilter,
        })



def catch_receipt_details(request, pk):
    catch_receipt = get_object_or_404(CatchReceipt, pk=pk)

    total_amount = int(catch_receipt.amount) + int(catch_receipt.overnight) + int(catch_receipt.return_fare) - int(catch_receipt.deduction) 
    total_ward = num2words(int(total_amount) , lang='ar')


    return render(request, 'financial/catch/catch_receipt_details.html',{
        'catch_receipt':catch_receipt,
        'total_amount':total_amount,
        'total_ward':total_ward,
        })

def add_catch_receipt(request):
    if request.method == 'POST':
        catch_receipt_form = AddCatch(request.POST, request.FILES)
        if catch_receipt_form.is_valid():
            form = catch_receipt_form.save()
            form.accountant = str(request.user)
            form.save()
            return redirect('catch_receipt_list')
    else:
        catch_receipt_form = AddCatch()

    return render(request, 'financial/catch/catch_receipt_add_edit.html',{'catch_receipt_form':catch_receipt_form})


def edit_catch_receipt(request, pk):
    catch_receipt = get_object_or_404(CatchReceipt, pk=pk)
    if request.method == 'POST':
        catch_receipt_form = AddCatch(request.POST, instance=catch_receipt)
        if catch_receipt_form.is_valid():
            catch_receipt_form.save()
            return redirect('catch_receipt_list')
    else:
        catch_receipt_form = AddCatch(instance=catch_receipt)

    return render(request, 'financial/catch/catch_receipt_add_edit.html',{'catch_receipt_form':catch_receipt_form})

def delete_catch_receipt(request, pk):
    catch_receipt = get_object_or_404(CatchReceipt, pk=pk)
    catch_receipt.delete()
    return redirect('all_catch_receipt_list')