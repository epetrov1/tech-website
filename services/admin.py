from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Services

class ServicesPostAdmin(SummernoteModelAdmin):  
    prepopulated_fields= {'slug':('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title','slug')
    summernote_fields = ('content')

admin.site.register(Services, ServicesPostAdmin)