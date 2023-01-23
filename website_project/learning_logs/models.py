from django.db import models

def __str__(self):
    """Return a simple string representing the entry."""
    return f"{self.text[:50]}..."