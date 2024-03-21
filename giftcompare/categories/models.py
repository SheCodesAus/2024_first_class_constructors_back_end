from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = "category"

    name = models.TextField()