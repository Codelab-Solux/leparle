from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


# class SignupForm(UserCreationForm):

#     def __init__(self, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#         self.fields["username"].help_text = ''
#         self.fields["email"].help_text = ''
#         self.fields["first_name"].help_text = ''
#         self.fields["last_name"].help_text = ''
#         self.fields["phone"].help_text = ''
#         self.fields["password1"].help_text = ''
#         self.fields["password2"].help_text = ''

#     class Meta:
#         model = CustomUser
#         fields = (
#             'username', 'email', 'first_name', 'last_name', 'password1', 'password2',
#         )
#         widgets = {
#             'username': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
#             'email': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
#             'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
#             'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
#             'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
#             'password1': forms.PasswordInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
#             'password2': forms.PasswordInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
#         }


class NewUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].help_text = ''
        self.fields["email"].help_text = ''
        self.fields["first_name"].help_text = ''
        self.fields["last_name"].help_text = ''
        self.fields["phone"].help_text = ''
        self.fields["password1"].help_text = ''
        self.fields["password2"].help_text = ''

    class Meta:
        model = CustomUser
        fields = (
            'username', 'email', 'first_name', 'last_name', 'phone', 'password1', 'password2', 'role','sector'
        )
        widgets = {
            'username': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'email': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'password1': forms.PasswordInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'password2': forms.PasswordInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'role': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'sector': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('__all__')
        exclude = ('role', 'groups', 'user_permissions',
                   'password', 'last_login', 'is_staff', 'is_superuser', 'is_active')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'email': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'username': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'role': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'sector': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
        }
class AdminEditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('__all__')
        exclude = ('groups', 'user_permissions',
                   'password', 'last_login', 'is_staff', 'is_superuser', )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'email': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'username': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'role': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'sector': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
        }


class RoleForm(forms.ModelForm):


    class Meta:
        model = Role
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'sec_level': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
        }
