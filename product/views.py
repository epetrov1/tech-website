from django.shortcuts import render
from . models import Product, ProductImages, Category, Factory
from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.db.models import Q, query
from django.utils.translation import gettext as _

#Globul function for Categories tree. Use it in "product/shop-fullwidth.html"
def categorys(request):
    category_globul = Category.objects.all()
    context = {
        'category_globul': category_globul,
    }
    return context




#Deatail view of category and subcategory from tree + related products of choosen category
class ProductsByCategoryView(DetailView, MultipleObjectMixin):
    model = Category
    template_name = "product/shop-fullwidth.html"
    paginate_by = 12


    def get_context_data(self, **kwargs):
        id = str(self.kwargs.get('slug'))
        object_list = Product.objects.prefetch_related('category').filter(category__slug=id)
        context = super(ProductsByCategoryView, self).get_context_data(object_list=object_list, **kwargs)
        return context




#Product by factory. List view all product. Detail for Factory
class FactoryDetailView(DetailView, MultipleObjectMixin):
    model = Factory
    template_name = "product/factory_detail.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        id = str(self.kwargs.get('slug'))
        object_list = Product.objects.select_related('factory').filter(factory__slug=id)
        context = super(FactoryDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context


#All factorys
class FactoryListView(ListView):
    model = Factory
    ordering = ['-name']
    template_name = "product/factory_list.html"
    paginate_by = 12



# Detail of product with all related products to same factory
class ProductDetailsView(DetailView, MultipleObjectMixin):
    model = Product
    template_name = "product/product-details.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        product = str(self.object.id)
        factory = str(self.object.factory.id)
        obj_pic = ProductImages.objects.select_related('product').filter(product__id=product)
        object_list = Product.objects.all().select_related('factory').filter(factory__id=factory)
        context = super(ProductDetailsView, self).get_context_data(object_list=object_list, obj_pic=obj_pic, **kwargs)
        print(id)
        return context




#Home page view
def home(request):
    category = Category.objects.all()
    products = Product.objects.all()
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'tech/index.html', {'context': context})


#Contact page view
def contacts(request):
    
    context = {
        
    }
    return render(request, 'tech/contact.html', {'context': context})

# Search in Product view
class SearchResultsView(ListView):
    model = Product
    template_name = 'product/search_template.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name_en__icontains=query) | Q(name_bg__icontains=query) | Q(name__icontains=query) | Q(description_en__icontains=query) | Q(description_bg__icontains=query) | Q(description__icontains=query) | Q(specification_en__icontains=query) | Q(specification_bg__icontains=query) | Q(specification__icontains=query)
        )
        return object_list
