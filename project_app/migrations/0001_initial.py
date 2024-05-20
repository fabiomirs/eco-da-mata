# Generated by Django 5.0.4 on 2024-05-20 02:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community_app', '0001_initial'),
        ('event_app', '0001_initial'),
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
                ('event_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_app.event')),
            ],
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_app.project')),
            ],
        ),
    ]
