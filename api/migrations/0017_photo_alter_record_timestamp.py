# Generated by Django 4.0.3 on 2022-03-29 08:04

import cloudinary.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_record_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.AlterField(
            model_name='record',
            name='timestamp',
            field=models.DateField(default=datetime.date(2022, 3, 29)),
        ),
    ]
