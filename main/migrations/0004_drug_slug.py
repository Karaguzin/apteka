# Generated by Django 4.2.5 on 2023-12-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_task_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='slug',
            field=models.SlugField(default='', max_length=255),
        ),
    ]