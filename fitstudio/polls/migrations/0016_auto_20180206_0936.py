# Generated by Django 2.0.1 on 2018-02-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20180206_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='name_text',
            field=models.CharField(max_length=200),
        ),
    ]
