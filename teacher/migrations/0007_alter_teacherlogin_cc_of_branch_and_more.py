# Generated by Django 4.0.5 on 2022-11-18 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0006_alter_branch_detail_fri_lec1_and_more'),
        ('teacher', '0006_alter_teacherlogin_cc_of_branch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherlogin',
            name='cc_of_branch',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_fri_lec1',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_fri_l1', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_fri_lec2',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_fri_l2', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_fri_lec3',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_fri_l3', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_fri_lec4',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_fri_l4', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_fri_lec5',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_fri_l5', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_fri_lec6',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_fri_l6', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_fri_lec7',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_fri_l7', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_fri_lec8',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_fri_l8', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_mon_lec1',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_mon_l1', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_mon_lec2',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_mon_l2', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_mon_lec3',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_mon_l3', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_mon_lec4',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_mon_l4', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_mon_lec5',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_mon_l5', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_mon_lec6',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_mon_l6', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_mon_lec7',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_mon_l7', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_mon_lec8',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_mon_l8', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_sat_lec1',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_sat_l1', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_sat_lec2',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_sat_l2', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_sat_lec3',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_sat_l3', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_sat_lec4',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_sat_l4', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_sat_lec5',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_sat_l5', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_sat_lec6',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_sat_l6', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_sat_lec7',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_sat_l7', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_sat_lec8',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_sat_l8', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_thurs_lec1',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_thurs_l1', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_thurs_lec2',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_thurs_l2', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_thurs_lec3',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_thurs_l3', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_thurs_lec4',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_thurs_l4', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_thurs_lec5',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_thurs_l5', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_thurs_lec6',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_thurs_l6', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_thurs_lec7',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_thurs_l7', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_thurs_lec8',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_thurs_l8', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_tues_lec1',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_tues_l1', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_tues_lec2',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_tues_l2', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_tues_lec3',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_tues_l3', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_tues_lec4',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_tues_l4', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_tues_lec5',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_tues_l5', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_tues_lec6',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_tues_l6', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_tues_lec7',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_tues_l7', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_tues_lec8',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_tues_l8', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_wed_lec1',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_wed_l1', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_wed_lec2',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_wed_l2', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_wed_lec3',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_wed_l3', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_wed_lec4',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_wed_l4', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_wed_lec5',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_wed_l5', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_wed_lec6',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_wed_l6', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_wed_lec7',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_wed_l7', to='branch.branch_detail'),
        ),
        migrations.AlterField(
            model_name='teacherlogin',
            name='teach_wed_lec8',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teach_wed_l8', to='branch.branch_detail'),
        ),
    ]
