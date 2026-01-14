from django import forms
from .models import Event
from django.core.exceptions import ValidationError
from django.utils import timezone

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=['name','date','time','description']
        
        def clean_date(self):
            date=self.clean_date['date']
            if date<timezone.now().date():
                raise ValidationError("Date cannot be in the past!")
            return date
