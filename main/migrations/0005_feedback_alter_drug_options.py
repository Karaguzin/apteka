# Generated by Django 4.2.5 on 2024-01-04 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_drug_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=25)),
                ('message', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='drug',
            options={'verbose_name': 'Лекарство', 'verbose_name_plural': 'Лекарства'},
        ),
    ]