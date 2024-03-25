from django.db import models
from categories.models import Category

# Create your models here.

class Gift(models.Model):
    class Meta:
        db_table = "gift"

    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.URLField()
    featured_time = models.DateTimeField(null=True)
    source_url = models.URLField()

    categories = models.ManyToManyField(
        Category,
        db_table="gift_category",
        related_name="+",
        symmetrical=False,
    )

