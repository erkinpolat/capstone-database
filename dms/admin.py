from django.contrib import admin
from .models import StudentJunior, Faculty

# Register your models here.

@admin.register(StudentJunior)
class StudentJuniorAdmin(admin.ModelAdmin):
	list_display = ['name', 'email']
	list_filter = ['name']

@admin.register(Faculty)
class StudentJuniorAdmin(admin.ModelAdmin):
	list_display = ['name', 'email']
	list_filter = ['name']