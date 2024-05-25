# Generated by Django 5.0.6 on 2024-05-24 21:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='login',
            old_name='senha',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='people',
            name='subcategory_key',
        ),
        migrations.AlterField(
            model_name='login',
            name='people_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='people_app.people'),
        ),
    ]