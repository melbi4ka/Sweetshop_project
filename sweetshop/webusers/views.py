from django.contrib.auth import views as auth_views, get_user_model, authenticate, login
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, request
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.shortcuts import render, redirect

from sweetshop.webusers.forms import UserCreateForm, UserEditForm


UserModel = get_user_model()

class SignUpView(views.CreateView):
    template_name = 'profile/signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse('index'))

class SignInView(auth_views.LoginView):
    template_name = "profile/signin.html"

class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')

class UserDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'profile/profile_details.html'
    model = UserModel


class UserEditView(views.UpdateView):
    template_name = 'profile/profile_edit.html'
    model = UserModel
    form_class = UserEditForm
    # fields = ('first_name', 'last_name', 'city', 'street', 'street_number', 'phone_number', "additional_address_info")

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={
            'pk': self.request.user.pk,
        })

class UserDeleteView(views.DeleteView):
    template_name = 'profile/profile_delete.html'
    model = UserModel
    success_url = reverse_lazy('index')

class NoProfileView(views.TemplateView):
    template_name = 'profile/profile_without_auth.html'

