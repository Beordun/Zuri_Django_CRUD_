from django import forms
from .models import blog

class blogForm (forms):
    class Meta:
        model = blog
