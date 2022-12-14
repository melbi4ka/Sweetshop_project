from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic as views

from sweetshop.blogpost.models import BlogPost
from sweetshop.main.forms import NewsSubscriptCreateForm
from sweetshop.main.models import AdditionalLinkInformation
from sweetshop.product.models import Product


class IndexView(views.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        qs = BlogPost.objects.all()
        searched_qs = []
        for search_term in ('tip', 'menu of', 'fruit menu', 'occassion'):
            searched_qs.append(qs.filter(title__icontains=search_term))

        context['searched_qs'] = searched_qs
        context['about_one'] = AdditionalLinkInformation. \
            objects.filter(section_name__iexact='Welcome to our site').get()
        context['about_two'] = AdditionalLinkInformation. \
            objects.filter(section_name__iexact='The food story').get()

        return context


class TermsOfUseView(views.TemplateView):
    template_name = 'main/additional_links.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['terms_of_use'] = AdditionalLinkInformation.objects.get(section_name='terms of use')
        return context


class HelpView(views.TemplateView):
    template_name = 'main/additional_links.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['help'] = get_object_or_404(AdditionalLinkInformation, section_name='help')
        return context


class ServicesView(views.TemplateView):
    template_name = 'main/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = get_object_or_404(AdditionalLinkInformation, section_name__iexact='services')
        return context


def newsletter(request):
    if request.method == 'GET':
        form = NewsSubscriptCreateForm()
    else:
        form = NewsSubscriptCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(
        request,
        'main/newsletter.html',
        context,
    )


def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = Product.objects.filter(name__icontains=query)
            blogposts = BlogPost.objects.filter(title__icontains=query)
            context = {
                'products': products,
                'blogposts': blogposts,
            }
            return render(request, 'main/search.html', context)
        else:
            return render(request, 'main/search.html')


def handler404_view(request, exception):
    return render(request, 'not-found.html', status=404)


def handler500_view(request):
    return render(request, 'not-found.html', status=500)
