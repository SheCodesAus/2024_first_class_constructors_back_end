# Generated by Django 5.0.3 on 2024-03-25 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]