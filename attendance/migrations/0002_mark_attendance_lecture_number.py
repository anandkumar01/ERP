# Generated by Django 4.0.5 on 2022-12-10 14:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark_attendance',
            name='lecture_number',
            field=models.IntegerField(default=2, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]