
from django.shortcuts import render
from . models import Services
from django.views.generic import ListView, DetailView

class ServicesDetailView(DetailView):
    model = Services

class ServicesListView(ListView):
    model = Services
    paginate_by = 12
    ordering = ['-date_create']