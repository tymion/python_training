# Generated by Django 2.0 on 2018-01-21 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_dayoftheweek_index_int'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activitydone',
            old_name='activityTimeTeble_key',
            new_name='activity_key',
        ),
        migrations.AlterField(
            model_name='activitydone',
            name='coachReplacement_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Coach'),
        ),
    ]
