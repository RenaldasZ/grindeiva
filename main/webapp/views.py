from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from . forms import ContactForm

class Index(TemplateView):
    template_name = "webapp/index.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)

class CalculatorView(TemplateView):
    template_name = "webapp/calculator.html"

class GaleryView(TemplateView):
    template_name = "webapp/galery.html"

class ContactsView(FormView):
    template_name = "webapp/contacts.html"
    form_class = ContactForm
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
    