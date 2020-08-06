# Generated by Django 3.0.2 on 2020-07-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectdata', '0019_auto_20200717_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('sym', models.CharField(max_length=30, null=True)),
                ('body', models.CharField(max_length=30, null=True)),
                ('degree_applying', models.CharField(max_length=10, null=True)),
                ('degree_separating', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='irsupport',
            name='body1',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
