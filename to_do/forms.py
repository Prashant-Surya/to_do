
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from to_do.models import Task


class LogInForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("email", "password")


class SignUpForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, *args, **kwargs):
        User.objects.create(self.cleaned_data)


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('completed', 'text')

        widgets = {
            'completed': forms.CheckboxInput(),
            'text': forms.Textarea(attrs={
                'wrap': 'off',
                'rows': '1',
                'placeholder': "Press enter to save the task"
            }),
        }
