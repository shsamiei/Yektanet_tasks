# Generated by Django 4.0.5 on 2022-07-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Advertisement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='nastaran',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
