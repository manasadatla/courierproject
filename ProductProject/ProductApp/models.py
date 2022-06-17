from django.db import models

# Create your models here.
class ProductDetails(models.Model):
    name=models.CharField(max_length=25)
    description=models.TextField()
    cost_per_item=models.FloatField()
    stock_quantity=models.IntegerField()
    volume = models.PositiveIntegerField(blank=True, null=False)

    def __str__(self):
        return self.name

