# Generated by Django 4.0.5 on 2023-02-05 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0008_mark_attendance_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark_attendance',
            name='topics',
            field=models.JSONField(blank=True, null=True),
        ),
    ]