# Generated by Django 2.2.24 on 2022-01-29 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twainlove', '0003_auto_20211213_0417'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='owner',
            field=models.CharField(default='test', max_length=60),
            preserve_default=False,
        ),
    ]
