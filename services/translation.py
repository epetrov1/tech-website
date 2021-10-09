from modeltranslation.translator import translator, TranslationOptions
from .models import Services

class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_fields = ('en', 'bg')

translator.register(Services, ServicesTranslationOptions)