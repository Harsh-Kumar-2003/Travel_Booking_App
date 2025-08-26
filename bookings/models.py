from django.db import models
from django.contrib.auth.models import User  # To link the Booking to a User
from django.core.validators import MinValueValidator
from django.utils import timezone

# Create your models here.
class TravelOption(models.Model):
    # Choices for the 'type' field
    TYPE_CHOICES = [
        ('FLIGHT', 'Flight'),
        ('TRAIN', 'Train'),
        ('BUS', 'Bus'),
    ]

    # Database fields for the TravelOption table
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()  # Date and Time of departure
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)]) # Price, must be positive
    # You can add more fields like 'arrival_time', 'duration', 'available_seats' later for bonus features.

    # String representation of the model (for Django admin and debug)
    def __str__(self):
        return f"{self.get_type_display()} from {self.source} to {self.destination} on {self.departure_time}"

class Booking(models.Model):
    # Choices for the 'status' field
    STATUS_CHOICES = [
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]

    # Link this booking to a specific User. If the user is deleted, delete their bookings too (CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Link this booking to a specific TravelOption. If the travel option is deleted, prevent deletion (PROTECT) to keep booking records.
    travel_option = models.ForeignKey(TravelOption, on_delete=models.PROTECT)
    number_of_seats = models.PositiveIntegerField(default=1)  # Must be at least 1
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    booking_date = models.DateTimeField(default=timezone.now)  # Automatically set to when the booking is created
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='CONFIRMED')

    def __str__(self):
        return f"Booking #{self.id} by {self.user.username} - {self.status}"

    # This method could be used to calculate total price automatically later
    # def save(self, *args, **kwargs):
    #     self.total_price = self.travel_option.price * self.number_of_seats
    #     super().save(*args, **kwargs)