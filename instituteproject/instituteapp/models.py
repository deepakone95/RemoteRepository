from django.db import models


class Course_instructors(models.Model):
    course_name=models.CharField(max_length=20)
    course_duration=models.CharField(max_length=20)
    instructor_name=models.CharField(max_length=20)
    instructor_experiance=models.CharField(max_length=20)
    start_date=models.DateField(max_length=20)
    start_time=models.TimeField(max_length=20)