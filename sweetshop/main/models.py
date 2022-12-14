from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from helpers.validators import validate_alphabet_characters


class SubscribedUser(models.Model):
    EMAIL_MAX_LENGTH = 30
    NAME_MAX_LENGTH = 50
    NAME_MIN_LENGTH = 3

    email = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=EMAIL_MAX_LENGTH,
    )
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.email}"

class Subsections(models.Model):
    SECTION_NAME_MAX_LENGTH = 30
    SECTION_NAME_MIN_LENGTH = 4
    SECTION_DESCRIPTION_MAX_LENGTH = 500

    subsection_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=SECTION_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(SECTION_NAME_MIN_LENGTH),
        )
    )

    subsection_description = models.TextField(
        max_length=SECTION_DESCRIPTION_MAX_LENGTH,
    )

    def __str__(self):
        return f"{self.subsection_name}"

    class Meta:
        verbose_name_plural = "Subsections"



class AdditionalLinkInformation(models.Model):
    SECTION_NAME_MAX_LENGTH = 30
    SECTION_NAME_MIN_LENGTH = 4
    SECTION_DESCRIPTION_MAX_LENGTH = 1000

    section_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=SECTION_NAME_MAX_LENGTH,
        validators=(
            validate_alphabet_characters,
            validators.MinLengthValidator(SECTION_NAME_MIN_LENGTH),
        )
    )
    subsections = models.ManyToManyField(
        Subsections,
        # null=True,
        blank=True,
    )

    section_description = models.TextField(
        max_length=SECTION_DESCRIPTION_MAX_LENGTH,
    )

    def __str__(self):
        return f"{self.section_name}"
