# Generated by Django 2.2.6 on 2019-11-24 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0003_auto_20191124_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='aliment',
            field=models.ManyToManyField(to='my_api.Aliment'),
        ),
        migrations.DeleteModel(
            name='Step',
        ),
    ]
