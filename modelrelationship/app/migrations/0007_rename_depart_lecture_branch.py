# Generated by Django 3.2.6 on 2021-10-06 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_department_lecture_depart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='depart',
            new_name='branch',
        ),
    ]
