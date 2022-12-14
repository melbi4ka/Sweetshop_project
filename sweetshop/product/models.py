from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.utils.text import slugify

# Create your models here.
UserModel = get_user_model()


class ProductType(models.Model):
    MIN_NAME_TYPE_LENGTH = 5
    MAX_NAME_TYPE_LENGTH = 40

    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 200

    name = models.CharField(
        max_length=MAX_NAME_TYPE_LENGTH,
        blank=False,
        null=False,
        validators=(
            validators.MinLengthValidator(MIN_NAME_TYPE_LENGTH),
        ),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=False,
        blank=False,
    )

    image = models.ImageField(
        upload_to='cakes/',
        null=False,
        blank=True,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("name",)


class Product(models.Model):

    MIN_NAME_TYPE_LENGTH = 5
    MAX_NAME_TYPE_LENGTH = 40

    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 200

    name = models.CharField(
        max_length=MAX_NAME_TYPE_LENGTH,
        blank=False,
        null=False,
        validators=(
            validators.MinLengthValidator(MIN_NAME_TYPE_LENGTH),
        ),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=False,
        blank=False,
    )

    image = models.ImageField(
        upload_to='pastrytypes/',
        null=False,
        blank=True,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )

    type = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type} -  {self.name}"

    class Meta:
        ordering = ("name",)
