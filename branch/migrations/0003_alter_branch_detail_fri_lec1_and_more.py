# Generated by Django 4.0.5 on 2022-11-09 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_branch_subjects_branch_subject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch_detail',
            name='fri_lec1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l1', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='fri_lec2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l2', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='fri_lec3',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l3', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='fri_lec4',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l4', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='fri_lec5',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l5', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='fri_lec6',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l6', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='fri_lec7',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l7', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='fri_lec8',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l8', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='mon_lec1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l1', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='mon_lec2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l2', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='mon_lec3',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l3', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='mon_lec4',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l4', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='mon_lec5',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l5', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='mon_lec6',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l6', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='mon_lec7',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l7', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='mon_lec8',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l8', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='sat_lec1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l1', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='sat_lec2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l2', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='sat_lec3',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l3', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='sat_lec4',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l4', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='sat_lec5',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l5', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='sat_lec6',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l6', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='sat_lec7',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l7', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='sat_lec8',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l8', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='thurs_lec1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l1', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='thurs_lec2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l2', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='thurs_lec3',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l3', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='thurs_lec4',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l4', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='thurs_lec5',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l5', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='thurs_lec6',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l6', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='thurs_lec7',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l7', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='thurs_lec8',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l8', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='tues_lec1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l1', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='tues_lec2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l2', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='tues_lec3',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l3', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='tues_lec4',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l4', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='tues_lec5',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l5', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='tues_lec6',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l6', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='tues_lec7',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l7', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='tues_lec8',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l8', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='wed_lec1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l1', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='wed_lec2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l2', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='wed_lec3',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l3', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='wed_lec4',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l4', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='wed_lec5',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l5', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='wed_lec6',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l6', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='wed_lec7',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l7', to='branch.branch_subjects'),
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='wed_lec8',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l8', to='branch.branch_subjects'),
        ),
    ]