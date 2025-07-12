from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Email Address')
    message = forms.CharField(widget=forms.Textarea, label='Message')
    subscribe = forms.BooleanField(required=False, label='Subscribe to newsletter')
    age = forms.IntegerField(required=False)

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError("You must be at least 18 years old.")
        return age
    # The method name must start with clean_ followed by the field name.
    # If validation fails, raise forms.ValidationError with a message.
    # Must return the cleaned (valid) data

# CharField: Text input
# EmailField: Email validation
# BooleanField: Checkbox
# widget=forms.Textarea: Multi-line input area

class RegistrationForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get('password')
        confirm_pwd = cleaned_data.get('confirm_password')

        if pwd and confirm_pwd and pwd != confirm_pwd:
            raise forms.ValidationError("Passwords do not match.")
        
        # Override clean() to access all cleaned data
        # Raise ValidationError to block the form submission
        # This is great for matching passwords, date ranges, etc.
