from django.contrib.auth.models import User
from django.forms import ModelForm

# Registration user form model
class UserRegistration(ModelForm):
    """docstring for UserRegistration"""
    def __init__(self, arg):
        super(UserRegistration, self).__init__()
        self.arg = arg

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

