# Generated by Django 2.0.1 on 2018-02-01 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20180201_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='alias_text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='coach',
            name='description_text',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
