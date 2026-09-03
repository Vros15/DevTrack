from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import JobApplication

User = get_user_model()

# Defines a form for user sign-up, extending Django's built-in UserCreationForm
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
# Defines a form for creating and updating job applications
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = (
            "company",
            "position",
            "status",
            "job_url",
            "notes",
            "applied_date",
        )