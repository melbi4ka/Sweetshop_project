<<<<<<< HEAD
from django.core import exceptions



def validate_alphabet_characters(value):
    for char in value.lower():
        if not char.isalpha() and char != " ":
            raise exceptions.ValidationError('Only letters are allowed')

=======
from django.core import exceptions



def validate_alphabet_characters(value):
    for char in value.lower():
        if not char.isalpha() and char != " ":
            raise exceptions.ValidationError('Only letters are allowed')

# def validate_only_letters(value):
#     for ch in value:
#         if not ch.isalpha():
#             raise exceptions.ValidationError('Only letters are allowed')
#
# def validate_only_digits(value):
#     for ch in value:
#         if not ch.isdigit():
#             raise exceptions.ValidationError('Only digits are allowed')
>>>>>>> 689920d351a5b28af45451f5dffca5bd6142ef67
