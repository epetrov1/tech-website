from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from django_summernote.admin import SummernoteModelAdmin
from . models import Category, Product, ProductImages, Factory



class CategoryAdmin(SummernoteModelAdmin, DraggableMPTTAdmin):
    prepopulated_fields= {'slug':('name',)}
    summernote_fields = ('description', 'description_bg', 'description_en')

admin.site.register(Category, CategoryAdmin)



class FactoryAdmin(SummernoteModelAdmin):
    list_display = ('name', 'data_order')
    sortable_field_name = "position"
    list_editable = ('data_order',)
    prepopulated_fields= {'slug':('name',)}
    summernote_fields = ('description', 'description_bg', 'description_en')

admin.site.register(Factory, FactoryAdmin)


class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages

class ProductAdmin(SummernoteModelAdmin):
    list_display = ('name', 'factory', 'top', 'new', 'data_order')
    list_editable = ('top', 'new', 'data_order')
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