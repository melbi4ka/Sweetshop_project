from django.urls import path

from sweetshop.blogpost.views import BlogPostView, CreateBlogPostView, EditBlogPostView, DeleteBlogPostView, \
    SingleBlogPostView

urlpatterns = (
    path("", BlogPostView.as_view(), name="blog post"),
    path("<int:pk>/", SingleBlogPostView.as_view(), name="single blog post"),
    path("create/", CreateBlogPostView.as_view(), name="create post"),
    path("edit/<int:pk>/", EditBlogPostView.as_view(), name="edit post"),
    path("delete/<int:pk>/", DeleteBlogPostView.as_view(), name="delete post"),
    path("success/", DeleteBlogPostView.as_view(), name="delete post"),
)