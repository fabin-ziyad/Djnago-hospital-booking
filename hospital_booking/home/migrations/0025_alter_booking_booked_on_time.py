# Generated by Django 4.0.6 on 2022-07-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_booking_booked_on_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Booked_On_Time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
