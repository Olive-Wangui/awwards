# Generated by Django 3.2.8 on 2021-10-24 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_ratings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tags',
            new_name='tag',
        ),
    ]
