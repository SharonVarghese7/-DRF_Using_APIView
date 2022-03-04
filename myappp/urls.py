from .views import registeredList
from django.urls import path

urlpatterns = [
    path('register/', registeredList.as_view(), name='register'),
]