# Generated by Django 4.2.6 on 2023-10-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_courses_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]