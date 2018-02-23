from django import forms
from django.forms import modelform_factory
from TaxApp.api import models

ResidentialAddressForm = modelform_factory(
    models.ResidentialAddress, exclude=('tax_payer',))

CompanyAddressForm = modelform_factory(
    models.CompanyAddress, exclude=('tax_payer',))

class UserEditForm(forms.ModelForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')

        if not self.user.check_password(old_password):
            raise forms.ValidationError("Incorrect Password")

        return old_password

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_new_password = self.cleaned_data.get('confirm_new_password')

        if new_password and (new_password is not confirm_new_password):
            raise forms.ValidationError('Passwords don\'t match')
        
        return confirm_new_password
    
    def save(self, commit=True):
       user = super().save(commit=False)

       new_password = self.cleaned_data.get('new_password')
       if new_password:
           user.set_password(new_password)

       if commit:
           user.save()

       return user

    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'username', 'email')
