# Generated by Django 5.0.6 on 2024-06-26 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_vendor_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
