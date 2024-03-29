# Generated by Django 5.0.3 on 2024-03-29 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0002_alter_gift_featured_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gift',
            name='featured_time',
        ),
        migrations.AddField(
            model_name='gift',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]