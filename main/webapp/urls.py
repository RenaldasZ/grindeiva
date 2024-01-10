from django.urls import path
from . views import Index, CalculatorView, GaleryView, ContactsView

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('calculator/', CalculatorView.as_view(), name="calculator"),
    path('galery/', GaleryView.as_view(), name="galery"),
    path('contacts/', ContactsView.as_view(), name="contacts"),
]