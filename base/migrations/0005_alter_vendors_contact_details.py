# Generated by Django 3.2.22 on 2023-12-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_historicalperformaces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendors',
            name='contact_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
