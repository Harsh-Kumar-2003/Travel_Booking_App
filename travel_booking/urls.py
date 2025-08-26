from django.contrib import admin
from django.urls import path, include
# Import the built-in views for authentication
from django.contrib.auth import views as auth_views
# We will import our own view for signup later
from bookings import views as bookings_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include Django's authentication URLs (login, logout, password management)
    # These will create URLs like /accounts/login/, /accounts/logout/
    path('accounts/', include('django.contrib.auth.urls')),
    # Add a URL for the signup page (we will create the view next)
    path('accounts/signup/', bookings_views.signup, name='signup'),
    # Include our app's URLs
    path('', include('bookings.urls')),
]