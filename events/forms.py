
from django import forms
from .models import Event
from django.core.exceptions import ValidationError
from django.utils import timezone

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'time', 'description']

    def clean_date(self):
        event_date = self.cleaned_data.get('date')

        if event_date < timezone.now().date():
            raise ValidationError("Check the date. You can only add upcoming events.")

        return event_date
