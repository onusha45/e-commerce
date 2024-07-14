from django.db import models
from category.models import *
# Create your models here.
class AddProduct(models.Model):
    Product_name = models.CharField(max_length=80)
    Description = models.TextField(default="")
    Product_img = models.ImageField(upload_to='AdminProducts/image', null=True)
    Expiry_Date = models.DateField()
    Stock_unit = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    Product_price = models.IntegerField( null=True)
    def __str__(self):
        return self.Product_name
    
