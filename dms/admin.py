from django.contrib import admin
from .models import StudentJunior

# Register your models here.

@admin.register(StudentJunior)
class StudentJuniorAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'email']
	list_filter = ['created']