from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()

class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email")
        field_classes = {
            "username": auth_forms.UsernameField
        }

class UserEditForm(auth_forms.UserChangeForm):
    password = None

    class Meta:
        model = UserModel
        fields = ("first_name", "last_name", "city", "street", "street_number", "phone_number", "additional_address_info")
        field_classes = {
            "username": auth_forms.UsernameField
        }
