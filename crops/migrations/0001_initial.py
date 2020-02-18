# Generated by Django 2.2.1 on 2020-01-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('start_date', models.DateField()),
                ('est_harvest', models.DateField()),
                ('problem', models.CharField(max_length=1000)),
            ],
        ),
    ]
