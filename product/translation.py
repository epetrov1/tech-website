from modeltranslation.translator import translator, TranslationOptions
from .models import Product, Category, Factory

class CategryTranslationOptions(TranslationOptions):
    fields = ('name', 'parent')
    required_fields = ('en', 'bg')

translator.register(Category, CategryTranslationOptions)

class ProductranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'specification')
    required_fields = ('en', 'bg')

translator.register(Product, ProductranslationOptions)

class FactoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
    required_fields = ('en', 'bg')

translator.register(Factory, FactoryTranslationOptions)