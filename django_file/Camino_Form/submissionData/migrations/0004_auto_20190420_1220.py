# Generated by Django 2.2 on 2019-04-20 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissionData', '0003_auto_20190420_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='status',
        ),
        migrations.AddField(
            model_name='loan',
            name='years',
            field=models.FloatField(help_text='Please Enter Years in Business', null=True),
        ),
    ]