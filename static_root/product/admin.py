from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from django_summernote.admin import SummernoteModelAdmin
from . models import Category, Product, ProductImages, Factory

from ordered_model.admin import OrderedModelAdmin


class CategoryAdmin(SummernoteModelAdmin, DraggableMPTTAdmin):
    prepopulated_fields= {'slug':('name',)}
    summernote_fields = ('description', 'description_bg', 'description_en')

admin.site.register(Category, CategoryAdmin)



class FactoryAdmin(SummernoteModelAdmin, OrderedModelAdmin):
    list_display = ('name',)
    prepopulated_fields= {'slug':('name',)}
    summernote_fields = ('description', 'description_bg', 'description_en')

admin.site.register(Factory, FactoryAdmin)


class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages

class ProductAdmin(SummernoteModelAdmin):
    list_display = ('name', 'factory', 'top', 'new')
    list_filter = ('factory__name', 'category__name',)
    search_fields = ('name',)
    list_per_page = 20
    prepopulated_fields= {'slug':('name',)}
    summernote_fields = ('description', 'specification', 'description_bg', 'description_en', 'specification_bg', 'specification_en')
    inlines = (ProductImagesAdmin, )
 
    class Meta:
       model = Product
 

admin.site.register(Product, ProductAdmin)

class ProductImagesAdmin(admin.ModelAdmin):
    pass

""" class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'factory', 'top', 'new')
    list_filter = ('factory',)
    search_fields = ('name',)
    

admin.site.register(Product, ProductAdmin) """