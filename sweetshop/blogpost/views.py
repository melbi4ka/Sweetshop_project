from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from sweetshop.blogpost.forms import CreateBlogPostForm, EditBlogPostForm
from sweetshop.blogpost.models import BlogPost


class BlogPostView(views.ListView):
    model = BlogPost
    template_name = 'blogpost/blog.html'
    paginate_by = 2


class SingleBlogPostView(views.DetailView):
    model = BlogPost
    template_name = 'blogpost/single_blogpost.html'


class CreateBlogPostView(LoginRequiredMixin, SuccessMessageMixin, views.CreateView):
    form_class = CreateBlogPostForm
    template_name = "blogpost/create_blog_post.html"
    login_url = 'login user'
    success_url = reverse_lazy("blog post")
    success_message = "Your blog post has been created"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)

        context = {
            "form": form,
        }
        return render(request, self.template_name, context)


class EditBlogPostView(LoginRequiredMixin, SuccessMessageMixin, views.UpdateView):
    model = BlogPost
    form_class = EditBlogPostForm
    template_name = "blogpost/edit_blog_post.html"
    login_url = 'login user'
    success_url = reverse_lazy("blog post")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pk'] = BlogPost.objects.filter(pk=self.kwargs.get('pk'))
        return context


class DeleteBlogPostView(LoginRequiredMixin, SuccessMessageMixin, views.DeleteView):
    model = BlogPost
    template_name = "blogpost/delete_blog_post.html"
    login_url = 'login user'
    success_url = reverse_lazy("blog post")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pk'] = BlogPost.objects.filter(pk=self.kwargs.get('pk'))
        return context
