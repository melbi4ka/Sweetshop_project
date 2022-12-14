from django.core import validators
from django.db import models

from helpers.validators import validate_alphabet_characters


class ContactForm(models.Model):
    NAME_MIN_LENGTH = 2
    NAME_MAX_LENGTH = 50
    SUBJECT_MAX_LENGTH = 50
    SUBJECT_MIN_LENGTH = 5
    MESSAGE_MAX_LENGTH = 500
    MESSAGE_MIN_LENGTH = 10

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            validate_alphabet_characters,
            validators.MinLengthValidator(NAME_MIN_LENGTH),
        )
    )
    subject = models.CharField(
        max_length=SUBJECT_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            validate_alphabet_characters,
            validators.MinLengthValidator(SUBJECT_MIN_LENGTH),
        )
    )

    email = models.EmailField(
        max_length=30,
        null=False,
        blank=False,
    )

    message = models.CharField(
        max_length=MESSAGE_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MESSAGE_MIN_LENGTH),
        )
    )

    date_received = models.DateField(
        auto_now_add=True,
    )

    reply = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"{self.subject} - {self.email}"

    class Meta:
        verbose_name = 'Contact Form'
