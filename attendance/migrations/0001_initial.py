# Generated by Django 4.0.5 on 2022-11-18 06:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0006_alter_branch_detail_fri_lec1_and_more'),
        ('student', '0002_alter_studentlogin_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='mark_attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('present', models.BooleanField(verbose_name='Present')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentlogin')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branch.branch_subjects')),
            ],
        ),
    ]
