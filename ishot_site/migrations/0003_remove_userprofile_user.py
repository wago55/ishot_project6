# Generated by Django 3.1.4 on 2020-12-26 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ishot_site', '0002_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]