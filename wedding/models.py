from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Client(models.Model):
    PACKAGE_OPTIONS = [
        ('Wedding', 'Wedding'),
        ('Engagement Shoot', 'Engagement Shoot'),
        ('Destination Wedding', 'Destination Wedding')
    ]
    name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    package = models.CharField(max_length=64, choices=PACKAGE_OPTIONS, default='Wedding')
    description = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_requested = models.DateTimeField(auto_now_add=False)
    approved = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Calendar(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dates", null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="dates", null=True, blank=True)
    event_title = models.CharField(max_length=64)
    event_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.event_title
    

class Note(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="notes", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField()

    def __str__(self):
        return self.note

class Package(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    deets = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
