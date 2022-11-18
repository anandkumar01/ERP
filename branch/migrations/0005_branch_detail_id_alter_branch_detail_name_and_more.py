# Generated by Django 4.0.5 on 2022-11-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0004_alter_branch_detail_mon_lec1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch_detail',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterUniqueTogether(
            name='branch_detail',
            unique_together={('name', 'batch')},
        ),
    ]