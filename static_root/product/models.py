from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from django.template.defaultfilters import slugify
from django.urls import reverse


from ordered_model.models import OrderedModel

#Main Category 
class Category(MPTTModel):
    name = models.CharField(max_length=250)
    pic = models.ImageField(upload_to='category', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug =models.SlugField(null=False, unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']
        
    class Meta:
        verbose_name_plural = 'category'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})



#Factotys model
class Factory(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='factorys')
    slug =models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('factory-detail', kwargs={'slug': self.slug})



#Product model
class Product(models.Model):
    name = models.CharField(max_length=250)
    category = TreeManyToManyField(Category, blank=True)
    images = models.FileField(blank=True)
    slug =models.SlugField(null=False, unique=True)
    description = models.TextField()
    specification = models.TextField()
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='factory', related_query_name='factory')
    top = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)

    #order_with_respect_to = ('factory', 'category')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('product-details', kwargs={'slug': self.slug})


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', related_query_name='product')
    images = models.FileField(upload_to='product-images')

    def __str__(self):
        return self.product.name
