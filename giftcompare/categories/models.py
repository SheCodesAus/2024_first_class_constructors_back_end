from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = "category"

    name = models.TextField(unique=True)

    def __str__(self):
        return self.name