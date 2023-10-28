from django.urls import path
from main.views import HomeView, AboutView, FeatureView, MenuView, Event, ContactView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('feature/', FeatureView.as_view(), name='feature'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('event/', Event.as_view(), name='event'),
    path('contact/', ContactView.as_view(), name='contact'),

]