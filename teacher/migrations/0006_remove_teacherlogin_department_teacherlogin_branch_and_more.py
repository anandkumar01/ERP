# Generated by Django 4.0.5 on 2022-12-18 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0010_alter_branch_subjects_unique_together_and_more'),
        ('teacher', '0005_remove_teacherlogin_isactive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherlogin',
            name='department',
        ),
        migrations.AddField(
            model_name='teacherlogin',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='cc_of_branch',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Class_Coordinator', to='branch.branch_detail'),
        ),
    ]