from django import forms
from .models import CustomUser,ContactMessage
from django.contrib.auth.forms import AuthenticationForm

class CustomRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)

    dob = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Date of Birth"
    )

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email','password','confirm_password','phone','dob','gender','height','weight','profile_image','skin_type','religion_type','location_type']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

class LoginForm(AuthenticationForm):
    pass

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }