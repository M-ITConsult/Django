from django.shortcuts import render

def index(request):
    """The home page."""
    return render(request, 'learning_logs/index.html')

def projects(request):
    """The projects page."""
    return render(request, 'learning_logs/projects.html')

def contact(request):
    """The contact page"""
    return render(request, 'learning_logs/contact.html')