# Generated by Django 3.1.1 on 2020-11-26 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0018_auto_20201126_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='nicheRank',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='college',
            name='usnRank',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='college',
            name='wsjRank',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
