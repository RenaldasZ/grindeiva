from typing import Any
from django.conf import settings
from django.http import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.core.mail import BadHeaderError, EmailMessage
from django.template.loader import get_template
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from . forms import ContactForm, PriceCalculatorForm
from . models import JobModel

class Index(TemplateView):
    template_name = "webapp/index.html"

class CalculatorView(TemplateView):
    template_name = "webapp/calculator.html"
    
class GaleryView(ListView):
    template_name = "webapp/galery.html"
    model = JobModel
    context_object_name = 'object_list'

class ContactsView(FormView):
    template_name = "webapp/contacts.html"
    success_url = reverse_lazy("contacts")
    form_class = ContactForm

    def form_valid(self, form):
        #TODO: create nice message, and concat full name and email into it
        message_template = get_template('email/message.html').render(context={
            "full_name": self.request.POST.get('full_name'),
            "email": self.request.POST.get('email'),
            "question": self.request.POST.get('question')
        })

        try:
            msg = EmailMessage(
                subject=self.request.POST.get('subject'), 
                body=message_template, 
                from_email=settings.EMAIL_HOST_USER, 
                to=[settings.EMAIL_CLIENT]
            )
            msg.content_subtype = "html"
            msg.send()
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        return HttpResponseRedirect(self.success_url)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
    

def calculate_preliminary_price(area_m2, thickness_cm):
    base_price_per_m2 = 4.5  # Base price per square meter in EUR
    extra_charge_per_cm = 0.20  # Extra charge per square meter if thickness is over 5 cm

    if thickness_cm > 5:
        excess_thickness = thickness_cm - 5
        total_price = area_m2 * (base_price_per_m2 + excess_thickness * extra_charge_per_cm)
    else:
        total_price = area_m2 * base_price_per_m2

    print(total_price)
    return total_price


def price_calculator(request):
    if request.method == 'POST':
        form = PriceCalculatorForm(request.POST)
        if form.is_valid():
            plotas = form.cleaned_data['plotas']
            storis = form.cleaned_data['storis']
            kaina = calculate_preliminary_price(plotas, storis)
            return render(request, 'webapp/result.html', {'kaina': kaina})
    else:
        form = PriceCalculatorForm()

    return render(request, 'webapp/calculator.html', {'form': form})