from django.core import exceptions



def validate_alphabet_characters(value):
    for char in value.lower():
        if not char.isalpha() and char != " ":
            raise exceptions.ValidationError('Only letters are allowed')

