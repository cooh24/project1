from dataclasses import field
from django.forms import ModelForm
from .models import Wildfire

class WildfireDataForm(ModelForm):
    class Meta:
        model = Wildfire
        fields = '__all__'