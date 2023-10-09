# Generated by Django 4.2.5 on 2023-10-09 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_course_courseold'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('talk_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.talk')),
                ('slots', models.IntegerField()),
            ],
            options={
                'verbose_name': 'curso',
                'verbose_name_plural': 'cursos',
            },
            bases=('core.talk',),
        ),
    ]
