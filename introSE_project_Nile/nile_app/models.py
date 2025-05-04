from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length = 100)
    details = models.CharField(max_length = 500)

class Item(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.name
