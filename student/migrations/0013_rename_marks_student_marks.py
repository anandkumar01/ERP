# Generated by Django 4.0.5 on 2023-01-02 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0014_branch_detail_pso_1_branch_detail_pso_2_and_more'),
        ('erp', '0017_alter_subjects_to1_alter_subjects_to2_and_more'),
        ('student', '0012_marks_branch_marks_semester'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='marks',
            new_name='student_marks',
        ),
    ]
