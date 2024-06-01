from django.urls import path
from .views import about_view, hobby_view, time_view

urlpatterns = [
    path('about/', about_view, name='about'),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', time_view, name='time'),
]