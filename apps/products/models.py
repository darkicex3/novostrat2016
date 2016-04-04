from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    technical_data_sheet = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    first_img = models.ImageField()

