# Generated by Django 2.2.6 on 2019-11-24 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='aliment',
        ),
        migrations.AddField(
            model_name='food',
            name='aliment',
            field=models.ManyToManyField(to='my_api.Aliment'),
        ),
    ]
