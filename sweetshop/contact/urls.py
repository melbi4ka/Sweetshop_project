from django.urls import path

from sweetshop.contact.views import ContactFormView, SubmitContactFormView

urlpatterns = [
    path('', ContactFormView.as_view(), name='contact'),
    path('form-submitted-successfully/', SubmitContactFormView.as_view(), name='submit contact'),
]