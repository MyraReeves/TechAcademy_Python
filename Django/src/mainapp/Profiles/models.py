from django.db import models

Prefix_Choices = {
    ('Mr.','Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Ms.', 'Ms.'),
    ('Miss', 'Miss'),
    ('Sir', 'Sir'),
    ('Dame', 'Dame'),
    ('Lord', 'Lord'),
    ('Lady', 'Lady'),
    ('Rev', 'Rev'),
    ('Dr.', 'Dr.'),
    ('Mx', 'Mx'),
}

# Create your models here.
class Profile(models.Model):
    Prefix = models.CharField(max_length=5, choices=Prefix_Choices)
    First_Name = models.CharField(max_length=100, default="Anonymous", blank=True, null=False)
    Last_Name = models.CharField(max_length=100, default="", blank=True, null=False)
    Email = models.EmailField(max_length=300, default="", blank=True)
    Username = models.CharField(max_length=100, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.Username