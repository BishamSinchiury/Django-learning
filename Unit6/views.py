from django.shortcuts import render
from .forms import ContactForm, RegistrationForm

def contact_view(request):
    form = ContactForm()
    return render(request, 'Unit6/contact.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process registration, e.g., save user
            return render(request, 'success.html')
    else:
        form = RegistrationForm()
    return render(request, 'Unit6/register.html', {'form': form})