# Generated by Django 4.2.5 on 2023-10-09 17:53

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='CourseOld',
        ),
    ]
