# Generated by Django 5.0.6 on 2024-06-13 01:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('institution', 'Institution'), ('physical person', 'Physical person')], max_length=20)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=800)),
                ('institutional_email', models.EmailField(max_length=100, unique=True)),
                ('personal_page_link', models.URLField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('category', models.CharField(choices=[('institution', 'Institution'), ('physical person', 'Physical person')], max_length=20)),
                ('subcategory_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people_app.subcategory')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]