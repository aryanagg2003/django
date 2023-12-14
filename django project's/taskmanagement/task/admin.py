from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','description','created_at')
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Task,TaskAdmin)
# Register your models here.
