# Generated by Django 2.1 on 2019-07-06 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='id',
        ),
        migrations.AlterField(
            model_name='payments',
            name='rpctno',
            field=models.IntegerField(help_text='Enter Receipt Number', primary_key=True, serialize=False),
        ),
    ]
