
from django.shortcuts import render
from . models import Projects
from django.views.generic import ListView, DetailView

class ProjectsDetailView(DetailView):
    model = Projects

class ProjectsListView(ListView):
    model = Projects
    paginate_by = 8
    ordering = ['-date_create']