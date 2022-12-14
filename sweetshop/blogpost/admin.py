from django.contrib import admin

from sweetshop.blogpost.forms import CreateBlogPostForm
from sweetshop.blogpost.models import BlogPost, Tag


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    ordering = ('-date_created',)
    list_display = ('id','title', 'author', 'date_created')
    list_filter = ('title', 'author')
    search_fields = ('title', 'text')
    sortable_by = ('id', 'title', 'date_created')



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
