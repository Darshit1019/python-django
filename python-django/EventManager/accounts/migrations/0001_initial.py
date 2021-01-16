# Generated by Django 3.1.4 on 2021-01-09 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=400, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('starttime_of_event', models.DateTimeField(null=True)),
                ('endtime_of_event', models.DateTimeField(null=True)),
                ('registration_deadline', models.DateTimeField(null=True)),
                ('host_email', models.EmailField(max_length=200)),
                ('host_password', models.CharField(max_length=200)),
            ],
        ),
    ]