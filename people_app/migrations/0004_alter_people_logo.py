# Generated by Django 5.0.6 on 2024-05-25 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people_app', '0003_people_logo_people_subcategory_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='logo',
            field=models.ImageField(blank=True, default=1, upload_to=''),
        ),
    ]
