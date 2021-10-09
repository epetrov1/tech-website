from django.urls import path
from . import views
from .views import FactoryDetailView, FactoryListView, ProductsByCategoryView, ProductDetailsView, SearchResultsView

urlpatterns = [
    path("categorys/<slug:slug>", ProductsByCategoryView.as_view(), name="category_detail"),
    path("factorys/", FactoryListView.as_view(), name="factorys"),
    path("factorys/<slug:slug>/", FactoryDetailView.as_view(), name="factory-detail"),
    path("product/<slug:slug>", ProductDetailsView.as_view(), name="product-details"),
    path("search/", SearchResultsView.as_view(), name="search-results"),
]
