# Generated by Django 4.0.5 on 2023-01-29 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0021_alter_question_paper_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='code',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
