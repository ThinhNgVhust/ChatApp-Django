# Generated by Django 3.1.7 on 2022-09-07 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mychatapp', '0003_auto_20220907_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='picture',
            new_name='pic',
        ),
    ]
