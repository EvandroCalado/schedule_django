# Generated by Django 5.0.2 on 2024-02-08 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]