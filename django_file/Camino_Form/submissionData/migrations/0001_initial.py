# Generated by Django 2.2 on 2019-04-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModelName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_field_name', models.CharField(help_text='Please Enter Your Full Name', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
                ('amount', models.IntegerField(help_text='Please Enter Loan Amount Required', max_length=20)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
