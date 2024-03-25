# Generated by Django 5.0.3 on 2024-03-24 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_car_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='delivery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_location', to='myapp.unique_location'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='pick_up',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pick_up_location', to='myapp.unique_location'),
        ),
    ]
