from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, View
from main.models import Menu, Home, About, Feature, Event, Contact

class HomeView(TemplateView):
    model = Home
    template_name = 'main/home.html'


class AboutView(ListView):
    template_name = 'main/about.html'
    model = About

class FeatureView(ListView):
    template_name = 'main/feature.html'
    model = Feature

class MenuView(ListView):
    template_name = 'main/menu.html'
    model = Menu


class Event(ListView):
    template_name = 'main/Events.html'
    model = Event

class ContactView(ListView):
    template_name = 'main/contact.html'
    model = Contact







    