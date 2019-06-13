from django.contrib import admin
from .models import Student, User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['handle', 'name', 'status', 'mentor','function_points', 'effort', 'report']

admin.site.register(Student, StudentAdmin)