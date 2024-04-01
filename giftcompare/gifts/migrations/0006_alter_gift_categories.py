# Generated by Django 5.0.3 on 2024-04-01 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_name'),
        ('gifts', '0005_alter_gift_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='categories',
            field=models.ManyToManyField(db_table='gift_category', related_name='+', to='categories.category'),
        ),
    ]
