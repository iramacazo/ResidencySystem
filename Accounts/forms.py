from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate


class BaseModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BaseModelForm, self).__init__(*args, **kwargs)
        # add common css classes to all widgets
        for field in iter(self.fields):
            # get current classes from Meta
            classes = self.fields[field].widget.attrs.get("class")
            if classes is not None:
                classes += " form-control"
            else:
                classes = "form-control"
            self.fields[field].widget.attrs.update({
                'class': classes
            })


class SignUpForm(UserCreationForm, BaseModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class LogInForm(AuthenticationForm, BaseModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
