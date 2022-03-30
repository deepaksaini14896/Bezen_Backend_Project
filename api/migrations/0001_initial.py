# Generated by Django 4.0.3 on 2022-03-28 18:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_fish', models.CharField(max_length=50)),
                ('species', models.CharField(max_length=50)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('timestamp', models.DateField(default=datetime.datetime(2022, 3, 28, 18, 20, 38, 956016))),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]