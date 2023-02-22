from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from password import *

def index(request):
    """The home page."""
    return render(request, 'learning_logs/index.html')

def projects(request):
    """The projects page."""
    return render(request, 'learning_logs/projects.html')

def contact(request):
    """The contact page"""
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('learning_logs/emails/contactform.html', {
                'name': name,
                'email': email,
                'message': message,
            })

            send_mail('Message from M-IT Consult Website', 'This is the message', email, ['EMAIL'], html_message=html)

            return redirect('/contact')
        else:
            form = ContactForm()

    return render(request, 'learning_logs/contact.html', {'form': form})