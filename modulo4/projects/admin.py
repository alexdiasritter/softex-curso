from django.contrib import admin
from projects.models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'user')
    search_fields = ('titulo', 'user__username')
    list_filter = ('user',)

admin.site.register(Project, ProjectAdmin)