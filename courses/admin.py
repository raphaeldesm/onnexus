from django.contrib import admin
from .models import Instructor, Course, Module, Content

class ContentInline(admin.TabularInline):
    model = Content
    extra = 1

class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1
    inlines = [ContentInline]

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'is_buyable')
    list_filter = ('is_buyable', 'instructor')
    search_fields = ('title', 'description')
    inlines = [ModuleInline]

admin.site.register(Instructor)
admin.site.register(Course, CourseAdmin)
admin.site.register(Module)
admin.site.register(Content)