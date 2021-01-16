# Generated by Django 3.1.4 on 2021-01-10 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210110_0104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event_registration',
            old_name='endtime_of_event',
            new_name='ending_date',
        ),
        migrations.RenameField(
            model_name='event_registration',
            old_name='starttime_of_event',
            new_name='starting_date',
        ),
        migrations.AddField(
            model_name='event_registration',
            name='host_password',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event_registration',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='event_registration',
            name='event_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event_registration',
            name='host_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='event_registration',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
