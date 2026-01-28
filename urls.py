from django.contrib import admin
from django.urls import path, include
from pastes.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),                  # Home page
    path('', include('pastes.urls')), # All other routes
]
