# Generated by Django 3.1.1 on 2020-10-08 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0006_auto_20201008_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='femaleEnrolled',
            field=models.IntegerField(default=0, verbose_name='female Enrolled'),
        ),
        migrations.AddField(
            model_name='college',
            name='maleEnrolled',
            field=models.IntegerField(default=0, verbose_name='Male Enrolled'),
        ),
    ]
