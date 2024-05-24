# Generated by Django 5.0.4 on 2024-05-24 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community_app', '0001_initial'),
        ('people_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desctiption', models.CharField(max_length=800)),
                ('social_network_link', models.URLField()),
                ('telephone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('community_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community_app.community')),
            ],
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people_app.people')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_app.project')),
            ],
        ),
    ]
