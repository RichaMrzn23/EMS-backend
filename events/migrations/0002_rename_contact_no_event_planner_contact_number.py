# Generated by Django 5.0.6 on 2024-06-20 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event_planner',
            old_name='contact_no',
            new_name='contact_number',
        ),
    ]
