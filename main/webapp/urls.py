from django.urls import path
from . views import Index, GaleryView, ContactsView, price_calculator

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('galery/', GaleryView.as_view(), name="galery"),
    path('contacts/', ContactsView.as_view(), name="contacts"),
    path('calculator/', price_calculator, name="calculator"),
]