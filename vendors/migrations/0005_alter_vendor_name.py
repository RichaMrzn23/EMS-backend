# Generated by Django 5.0.6 on 2024-06-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_alter_vendor_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
