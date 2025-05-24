from django import forms
from .models import CustomUser , Contact
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

# Registration Form
class UserRegistrationForm(UserCreationForm):
    agree_terms = forms.BooleanField(
        required=True,
        label="I agree to the Terms & Conditions",
        error_messages={'required': 'You must agree to the terms to register.'}
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput, 
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput, 
        label="Confirm Password"
    )

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        # Remove help text for password fields
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    class Meta:
        model = CustomUser
        fields = ('username', 'email' , 'password1' , 'password2')
        
# Login Form Using Email 
class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

#Contact-Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']

    # Add custom validation for phone number (optional but must be valid if provided)
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone and not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only numbers!")
        return phone

# User-profile Form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_image', 'email', 'username', 'phone_number', 'date_of_birth']