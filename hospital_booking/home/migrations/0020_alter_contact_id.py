# Generated by Django 4.0.6 on 2022-07-29 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_contact_delete_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
