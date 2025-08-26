from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number_of_seats']  # User only needs to select seats
        labels = {
            'number_of_seats': 'Number of Seats'
        }
        widgets = {
            'number_of_seats': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'})
        }