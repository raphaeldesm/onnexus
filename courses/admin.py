from django.contrib import admin
from .models import Instructor, Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'is_buyable')
    list_filter = ('is_buyable', 'instructor')
    search_fields = ('title', 'description')

admin.site.register(Instructor)
admin.site.register(Course, CourseAdmin)