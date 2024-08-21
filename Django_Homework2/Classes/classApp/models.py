from django.db import models


# Create your models here.
class UniversityClass(models.Model):
    title = models.CharField(max_length=70, default="",blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=100, default="", blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    # Model manager:
    object = models.Manager()

    # Object values (tuple of class title followed by instructor name) displayed as a string:
    def __str__(self):
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)


# Sets exact text to display in browser
# Removes the added 's' that Django appends to model names in the browser
class Meta:
    verbose_name_plural = "University Classes"
