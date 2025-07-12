from django.contrib import admin
from .models import Task, Student
# Register your models here.

#register the model
admin.site.register(Task)

#customized registration
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email')
    search_fields = ('name', 'email')
    list_filter = ('age',)

admin.site.register(Student, StudentAdmin)

# list_display shows fields as columns in the list view
# search_fields adds a search box for these fields
# list_filter adds sidebar filters for quick filtering

admin.site.site_header = "ADCS Admin Panel"
admin.site.site_title = "ADCS Portal"
admin.site.index_title = "Welcome to the Admin Dashboard"


