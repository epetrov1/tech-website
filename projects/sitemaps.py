from django.contrib.sitemaps import Sitemap
from .models import Projects
 
 
class ProjectsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'
    i18n = True

    def items(self):
        return Projects.objects.all()

    def lastmod(self, obj):
        return obj.date_created