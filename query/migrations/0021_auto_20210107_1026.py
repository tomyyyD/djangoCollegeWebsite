# Generated by Django 3.1.1 on 2021-01-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0020_college_avgfinaid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='avgFinAid',
        ),
        migrations.AddField(
            model_name='college',
            name='froshAppForAid',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='college',
            name='froshAvgFinAid',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='college',
            name='froshGotFinAid',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='college',
            name='totalAppForAid',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='college',
            name='totalAvgFinAid',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='college',
            name='totalGotFinAid',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='college',
            name='totalStudents',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
