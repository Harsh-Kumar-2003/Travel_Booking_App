from django.urls import path
from . import views

app_name = 'bookings'  # This is a namespace for our app's URLs

urlpatterns = [
    path('', views.home_view, name='home'),
    path('travel/', views.TravelListView.as_view(), name='travel_list'),
    path('my-bookings/', views.BookingListView.as_view(), name='booking_list'),
    path('book/<int:travel_id>/', views.book_travel, name='book_travel'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]