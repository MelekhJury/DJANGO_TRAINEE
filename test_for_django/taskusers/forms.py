from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=70)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=70)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=70)

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  )

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__()

        self.fields['username'].widget.attrs ['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
