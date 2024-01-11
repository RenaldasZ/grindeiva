from typing import Any
from django.conf import settings
from django.http import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.core.mail import BadHeaderError, EmailMessage
from django.template.loader import get_template
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
    