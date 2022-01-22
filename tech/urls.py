"""tech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from product import views
from product.sitemaps import ProductSitemap, CategorySitemap, FactorySitemap
from projects.sitemaps import ProjectsSitemap
from services.sitemaps import ServicesSitemap, StaticSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from fiber.views import page
from fiber.sitemaps import FiberSitemap

def trigger_error(request):
    division_by_zero = 1 / 0

sitemaps = {
    'product': ProductSitemap,
    'category': CategorySitemap,
    'factory': FactorySitemap,
    'projects': ProjectsSitemap,
    'services': ServicesSitemap,
    'static': StaticSitemap,
}

urlpatterns = [
    path("", views.home, name="home"),
    path('api/v2/', include('fiber.rest_api.urls')),
    path('admin/fiber/', include('fiber.admin_urls')),
    path("contacts/", views.contacts, name="contacts"),
    path('bugs-best-techsite/', admin.site.urls),
    path("products/", include('product.urls')),
    path("services/", include('services.urls')),
    path("projects/", include('projects.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('sitemap.xml', sitemap, {'fiber': FiberSitemap, 'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
        path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    re_path('', page),
    
]

urlpatterns += i18n_patterns (
    path("", views.home, name="home"),
    path('api/v2/', include('fiber.rest_api.urls')),
    path('admin/fiber/', include('fiber.admin_urls')),
    path("contacts/", views.contacts, name="contacts"),
    path("products/", include('product.urls')),
    path("services/", include('services.urls')),
    path("projects/", include('projects.urls')),
    path('summernote/', include('django_summernote.urls')),
    re_path('', page),
    
)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)