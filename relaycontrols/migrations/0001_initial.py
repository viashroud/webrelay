# Generated by Django 2.0.2 on 2018-02-14 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Relay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin_number', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('current_state', models.BooleanField()),
            ],
        ),
    ]
