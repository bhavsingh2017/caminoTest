# Generated by Django 2.2 on 2019-04-21 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissionData', '0004_auto_20190420_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='business',
            field=models.CharField(default='none', help_text='Type of Business', max_length=20),
            preserve_default=False,
        ),
    ]