# Generated by Django 2.1.5 on 2019-01-14 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='profile',
        ),
    ]
