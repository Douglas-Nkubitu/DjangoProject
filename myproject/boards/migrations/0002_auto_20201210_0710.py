# Generated by Django 3.1.4 on 2020-12-10 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]