from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from sweetshop.webusers.forms import UserCreateForm, UserEditForm

# Register your models here.
UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    add_form = UserCreateForm

    ordering = ('username',)
    list_filter = ('username', "is_staff")
    search_fields = ('username', 'first_name', 'last_name', 'email', 'city',)
    sortable_by = ('id', 'username', 'last_name')

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'username',
                    'password',
                ),
            }),
        (
            'Personal info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'city',
                    'street',
                    'street_number',
                    'additional_address_info',
                    'phone_number',

                ),
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            'Important dates',
            {
                'fields': (
                    'last_login',
                    'date_joined',
                ),
            },
        ),
    )

    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)
