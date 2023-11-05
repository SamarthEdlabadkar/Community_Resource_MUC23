from django.db import models

# Create your models here.
class Food_Places(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=150)
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    image = models.TextField(max_length=400, null =True, blank=True)
    
    def __str__(self):
        return self.name+":"+self.category

class Resources(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name