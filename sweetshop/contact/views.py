from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from sweetshop.contact.forms import ContactFormForm
from sweetshop.contact.models import ContactForm


class ContactFormView(views.CreateView):
    template_name = 'contact/contact.html'
    model = ContactForm
    form_class = ContactFormForm
    success_url = reverse_lazy('submit contact')


class SubmitContactFormView(views.TemplateView):
    template_name = 'contact/submit_contact.html'
    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)
        context['object'] = ContactForm.objects.order_by('-id')[0]
        return context

