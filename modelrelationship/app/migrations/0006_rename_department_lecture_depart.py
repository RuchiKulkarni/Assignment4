# Generated by Django 3.2.7 on 2021-10-05 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_depart_lecture_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='department',
            new_name='depart',
        ),
    ]
