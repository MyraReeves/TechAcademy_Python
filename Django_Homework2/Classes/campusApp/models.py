from django.db import models


# Create your models here.
class UniversityCampus(models.Model):
    Campus_Name = models.CharField(max_length=50, default="", blank=True, null=False)
    City = models.CharField(max_length=60, default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)
    Campus_ID = models.IntegerField(default="", blank=True, null=False)

    # Model manager:
    object = models.Manager()

    # Displays the as a string:
    def __str__(self):
        return self.Campus_Name

    # Sets exact text to display in admin panel in browser:
    class Meta:
        verbose_name_plural = "University Campus"
