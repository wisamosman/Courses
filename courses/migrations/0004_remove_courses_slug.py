# Generated by Django 4.2.6 on 2023-10-21 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_courses_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='slug',
        ),
    ]
