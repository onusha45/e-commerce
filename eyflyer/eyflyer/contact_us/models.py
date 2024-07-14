from django.db import models

# Create your models here.
class Contactus(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default = 0)
    message = models.TextField(max_length=300)
    
    def __str__(self):
        return self.name