from django.urls import path
from . views import Index, GaleryView, ContactsView, CalculatorView

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('galery/', GaleryView.as_view(), name="galery"),
    path('contacts/', ContactsView.as_view(), name="contacts"),
    path('calculator/', CalculatorView.as_view(), name="calculator"),
]