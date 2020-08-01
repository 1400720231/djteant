from django.db import models

# Create your models here.
from django_multitenant.fields import *
from django_multitenant.models import *


class Store(TenantModel):
    tenant_id = 'id'
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=50)


class Product(TenantModel):
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    tenant_id = 'store_id'
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta(object):
        unique_together = ["id", "store"]


class Purchase(TenantModel):
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    tenant_id = 'store_id'
    product_purchased = TenantForeignKey(Product, on_delete=models.PROTECT)


class Prodetail(TenantModel):
    tenant_id = 'product_id'
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
