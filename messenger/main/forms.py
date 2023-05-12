from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Message

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

class SendMessageForm(forms.ModelForm):
    recipient = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def clean_recipient(self):
        recipient = self.cleaned_data['recipient']
        try:
            user = User.objects.get(username=recipient)
        except User.DoesNotExist:
            raise forms.ValidationError("User does not exist")
        return user

    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']