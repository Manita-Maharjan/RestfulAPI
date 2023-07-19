from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    decription = models.TextField()
    price = models.IntegerField()

    def __str__ (self):
        return self.name #it saves object as product name in database i.e. if we dont write this it will show as product.object1 which will change into product name



    
