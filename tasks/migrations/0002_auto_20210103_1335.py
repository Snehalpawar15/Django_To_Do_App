# Generated by Django 2.0.2 on 2021-01-03 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Created',
            new_name='created',
        ),
    ]
