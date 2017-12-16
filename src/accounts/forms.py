from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Registration user form model
# Inherit from UserCreationForm
class UserRegistration(UserCreationForm):
    # add required to email feild
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]
    """
    def save(self, commit=True):
        user = super(UserRegistration, self).save(commit=False)
        # process the data in form.cleaned_data as required
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user.set_password(password)

        if commit:
            # save user to database
            user.save()
    """

