# Generated by Django 4.0.4 on 2022-06-19 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watch_app', '0005_alter_neighborhood_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='block',
            new_name='street',
        ),
    ]
