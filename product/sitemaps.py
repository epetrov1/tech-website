from django.contrib.sitemaps import Sitemap
from .models import Product, Category, Factory
 
 
class ProductSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'
    i18n = True

    def items(self):
        return Product.objects.all()




class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'
    i18n = True

    def items(self):
        return Category.objects.all()

class FactorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'
    i18n = True

    def items(self):
        return Factory.objects.all()


