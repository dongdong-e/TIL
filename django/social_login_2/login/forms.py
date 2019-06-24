from django import forms
from django.contrib.auth.models import User



class UserCustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields