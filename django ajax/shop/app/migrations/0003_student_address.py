# Generated by Django 4.0.6 on 2022-07-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
