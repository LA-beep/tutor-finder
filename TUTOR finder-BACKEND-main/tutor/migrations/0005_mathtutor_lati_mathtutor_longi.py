# Generated by Django 4.0.1 on 2022-01-13 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0004_mathtutor_dis_mathtutor_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='mathtutor',
            name='lati',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='mathtutor',
            name='longi',
            field=models.FloatField(default=0.0),
        ),
    ]
