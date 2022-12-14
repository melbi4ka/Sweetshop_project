from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Tag(models.Model):
    MAX_LEN_NAME = 20
    name = models.CharField(
        max_length=MAX_LEN_NAME,
    )

    def __str__(self):
        return f"{self.pk} - {self.name}"


class BlogPost(models.Model):
    MAX_LEN_TITLE = 150
    MAX_LEN_TEXT = 1000

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        unique=True,
        null=False,
        blank=False,
    )

    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    text = models.TextField(
        max_length=MAX_LEN_TEXT,
        null=False,
        blank=False,
    )

    date_created = models.DateField(
        auto_now_add=True,
    )

    blog_image = models.ImageField(
        upload_to='blogimages/',
        null=True,
        blank=True,
        verbose_name="Image"
    )

    tagged_posts = models.ManyToManyField(
        Tag,
        blank=True,
    )

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.title} - {self.author}"
