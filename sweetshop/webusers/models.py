from django.contrib.auth import models as auth_models, get_user_model
from django.core import validators
from django.db import models

from sweetshop.webusers.validators import validate_only_letters, validate_only_digits


# from helpers.validators import validate_only_letters, validate_only_digits



class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30

    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        null=True,
        blank=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        null=True,
        blank=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
        null = False,
        blank=False,
    )

    city = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        validators=(
            validate_only_letters,
        )
    )


    street = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    street_number = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        validators=(
            validate_only_digits,
        )
    )
    additional_address_info = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    @property
    def get_full_address(self):
        if self.city and self.street and self.street_number:
            return f"{self.city}, {self.street} N{self.street_number}"
        return None

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
        else:
            return f"{self.username}"




