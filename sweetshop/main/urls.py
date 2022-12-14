from django.urls import path

from sweetshop.main.views import IndexView, newsletter, search, HelpView, TermsOfUseView, ServicesView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('newsletter/',  newsletter, name='newsletters'),
    path('search/',  search, name='search'),
    path('help/',  HelpView.as_view(), name='help'),
    path('terms-of-use/',  TermsOfUseView.as_view(), name='terms of use'),
    path('services/',  ServicesView.as_view(), name='services'),
)
