from django.contrib import admin
from .models import Course_instructors

class Course_instructor_display(admin.ModelAdmin):
    list_display = [
        'course_name',
        'course_duration',
        'instructor_name',
        'instructor_experiance',
        'start_date',
        'start_time'
    ]
admin.site.register(Course_instructors,Course_instructor_display)
