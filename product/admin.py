from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from django_summernote.admin import SummernoteModelAdmin
from . models import Category, Product, ProductImages, Factory

class CategoryAdmin(DraggableMPTTAdmin):
    prepopulated_fields= {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)


class FactoryAdmin(SummernoteModelAdmin):
    list_display = ('name',)
    prepopulated_fields= {'slug':('name',)}
    summernote_fields = ('description')

admin.site.register(Factory, FactoryAdmin)


class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages

class ProductAdmin(SummernoteModelAdmin):
    list_display = ('name', 'factory', 'top', 'new')
    prepopulated_fields= {'slug':('name',)}
    summernote_fields = ('description', 'specification')
    inlines = [ProductImagesAdmin]
 
    class Meta:
       model = Product
 

admin.site.register(Product, ProductAdmin)

class ProductImagesAdmin(admin.ModelAdmin):
    pass