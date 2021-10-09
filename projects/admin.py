from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Projects

class ProjectsPostAdmin(SummernoteModelAdmin):  
    prepopulated_fields= {'slug':('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title','slug')
    summernote_fields = ('content', 'content_bg', 'content_en')

admin.site.register(Projects, ProjectsPostAdmin)