# Generated by Django 2.0.5 on 2018-06-24 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_pullrequest_closed_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='conduct_file',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='repository',
            name='contributing_file',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='repository',
            name='issue_template',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='repository',
            name='license_file',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='repository',
            name='pull_request_template',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='repository',
            name='readme',
            field=models.BooleanField(default=False),
        ),
    ]
