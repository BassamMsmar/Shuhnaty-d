from django.shortcuts import render

# Create your views here.
def financial_list(request):
    return render(request, 'financial/financial-list.html')