# Generated by Django 2.2.6 on 2019-11-24 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0008_auto_20191124_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('aliment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_api.Aliment')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_api.Food')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='aliment',
            field=models.ManyToManyField(blank=True, through='my_api.Step', to='my_api.Aliment'),
        ),
    ]
