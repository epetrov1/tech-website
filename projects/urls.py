from django.urls import path, include
from .views import ProjectsDetailView, ProjectsListView



urlpatterns = [
    path('<slug:slug>/', ProjectsDetailView.as_view(), name="detail_projects"),
    path('', ProjectsListView.as_view(), name="projects"),
]