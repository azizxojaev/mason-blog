from django.urls import path
from .views import home_page, about_page, timeline_page, contact_page

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('timeline/', timeline_page, name='timeline'),
    path('contact/', contact_page, name='contact'),
]
