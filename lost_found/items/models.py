from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models


class FoundItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    contact_number = models.CharField(max_length=15)
    location = models.CharField(max_length=200)
    date_found = models.DateField()
    image = models.ImageField(upload_to='found_items/', blank=False)

    def __str__(self):
        return self.title