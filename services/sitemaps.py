from django.contrib.sitemaps import Sitemap
from .models import Services
from django.urls import reverse
 
 
class ServicesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'
    i18n = True

    def items(self):
        return Services.objects.all()

    def lastmod(self, obj):
        return obj.date_created


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'
    i18n = True

    def items(self):
        return ['home', 'contacts']

    def location(self, item):
        return reverse(item)