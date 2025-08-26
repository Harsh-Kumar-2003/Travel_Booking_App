from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin  # To protect views for logged-in users only
from .models import TravelOption, Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from .models import TravelOption, Booking

@login_required
def book_travel(request, travel_id):
    travel_option = get_object_or_404(TravelOption, id=travel_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Create booking but don't save yet
            booking = form.save(commit=False)
            booking.user = request.user
            booking.travel_option = travel_option
            booking.total_price = travel_option.price * booking.number_of_seats
            booking.save()
            
            messages.success(request, f'Booking confirmed for {travel_option}!')
            return redirect('bookings:booking_list')
    else:
        form = BookingForm()
    
    return render(request, 'bookings/book_travel.html', {
        'form': form,
        'travel_option': travel_option
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in automatically after signup
            return redirect('bookings:home')  # Redirect to home page
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Create your views here.
def home_view(request):
    """A simple view for the website's home page"""
    return render(request, 'bookings/home.html')

class TravelListView(ListView):
    """View to display a list of all available travel options with filtering"""
    model = TravelOption
    template_name = 'bookings/travel_list.html'
    context_object_name = 'travel_options'

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Get filter parameters from GET request
        travel_type = self.request.GET.get('type')
        source = self.request.GET.get('source')
        destination = self.request.GET.get('destination')
        date = self.request.GET.get('date')
        
        # Apply filters if they exist
        if travel_type:
            queryset = queryset.filter(type=travel_type)
        if source:
            queryset = queryset.filter(source__icontains=source)
        if destination:
            queryset = queryset.filter(destination__icontains=destination)
        if date:
            queryset = queryset.filter(departure_time__date=date)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass current filter values back to template to pre-fill the form
        context['current_filters'] = {
            'type': self.request.GET.get('type', ''),
            'source': self.request.GET.get('source', ''),
            'destination': self.request.GET.get('destination', ''),
            'date': self.request.GET.get('date', ''),
        }
        return context

class BookingListView(LoginRequiredMixin, ListView):
    """View to display a list of the logged-in user's bookings.
    LoginRequiredMixin ensures only logged-in users can access this page."""
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'

    # This method customizes the queryset to only show the current user's bookings
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    # Only allow cancellation of confirmed bookings
    if booking.status == 'CONFIRMED':
        booking.status = 'CANCELLED'
        booking.save()
        messages.success(request, f'Booking #{booking_id} has been cancelled.')
    else:
        messages.warning(request, f'Booking #{booking_id} cannot be cancelled.')
    
    return redirect('bookings:booking_list')