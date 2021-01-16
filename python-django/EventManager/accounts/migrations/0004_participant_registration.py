# Generated by Django 3.1.4 on 2021-01-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210111_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_name', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=200, null=True)),
                ('participant_email', models.EmailField(max_length=254, null=True)),
                ('numberof_participant', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('events', models.ManyToManyField(to='accounts.Event_Registration')),
            ],
        ),
    ]