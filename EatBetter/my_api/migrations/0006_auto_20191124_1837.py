# Generated by Django 2.2.6 on 2019-11-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0005_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='aliment',
            field=models.ManyToManyField(through='my_api.Step', to='my_api.Aliment'),
        ),
    ]
