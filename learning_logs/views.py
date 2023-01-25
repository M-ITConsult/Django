from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    """The home page."""
    return render(request, 'learning_logs/index.html')

def projects(request):
    """The projects page."""
    return render(request, 'learning_logs/projects.html')

def contact(request):
    """The contact page"""
    if request.method == 'POST':
        message = request.POST['message']
        reciver = settings.EMAIL_HOST_USER

        send_mail(message, reciver, fail_silently=False, recipient_list=request.POST['email'])
    return render(request, 'learning_logs/contact.html')