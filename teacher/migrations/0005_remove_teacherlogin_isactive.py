# Generated by Django 4.0.5 on 2022-12-13 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_teacherlogin_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherlogin',
            name='isactive',
        ),
    ]
