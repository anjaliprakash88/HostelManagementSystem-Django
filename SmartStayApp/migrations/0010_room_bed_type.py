# Generated by Django 5.0.2 on 2024-02-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartStayApp', '0009_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='bed_type',
            field=models.CharField(choices=[('single', 'Single Bed'), ('double', 'Double Bed')], default='single', max_length=10),
        ),
    ]