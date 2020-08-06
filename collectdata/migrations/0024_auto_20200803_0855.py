# Generated by Django 3.0.2 on 2020-08-03 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectdata', '0023_auto_20200803_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boostangle',
            name='boost_angle',
        ),
        migrations.AddField(
            model_name='boostangle',
            name='boost_symbol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bracketedc',
            name='symbol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c',
            name='symbol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gasgiant',
            name='symbol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='irsupport',
            name='sym',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moon',
            name='sym',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='multiplesquare',
            name='symbol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opposition',
            name='symbol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sextile',
            name='symbol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trine',
            name='symbol',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
