from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User
from django.utils import timezone


class Order(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(null=False, default=timezone.now())
    status = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.title)
