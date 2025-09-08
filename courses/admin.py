from django.contrib import admin
from .models import Course, Student, Enrollment, Module, Feedback


class ModuleInline(admin.TabularInline):   # Inline form for modules
    model = Module
    extra = 1   # how many empty forms to show


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    list_filter = ('start_date', 'end_date')
    inlines = [ModuleInline]   # show modules inside course admin


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'enrollment_date')


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_on')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')


# 🔹 New Feedback Admin
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('course', 'created_at')
