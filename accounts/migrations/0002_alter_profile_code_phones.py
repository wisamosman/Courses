# Generated by Django 4.2.6 on 2023-11-03 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.generate_code


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.CharField(default=utils.generate_code.generate_code, max_length=10),
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_phones', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]