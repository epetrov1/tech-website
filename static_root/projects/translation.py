from modeltranslation.translator import translator, TranslationOptions
from .models import Projects

class ProjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_fields = ('en', 'bg')

translator.register(Projects, ProjectsTranslationOptions)