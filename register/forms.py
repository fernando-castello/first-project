from django import forms
from register.models import Email
class contact(forms.ModelForm):
    email = forms.EmailField(max_length=70,label = "Email")

    class Meta:
        model = Email
        fields =('email',)
