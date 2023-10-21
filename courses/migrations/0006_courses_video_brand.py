# Generated by Django 4.2.6 on 2023-10-21 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0005_courses_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='brand')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('cours', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cours_brand', to='courses.courses')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_brand', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
