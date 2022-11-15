from django.urls import path
from .views import financial_list


urlpatterns = [
    path('financial/',financial_list, name='financial_list' ),
]