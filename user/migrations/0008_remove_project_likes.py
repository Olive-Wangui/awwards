# Generated by Django 3.2.8 on 2021-10-26 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20211025_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='likes',
        ),
    ]
