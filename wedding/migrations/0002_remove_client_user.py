# Generated by Django 4.2.3 on 2023-08-16 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
    ]
