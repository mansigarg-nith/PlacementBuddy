# Generated by Django 4.1.2 on 2022-10-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='anonymity',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experience',
            name='exp',
            field=models.TextField(default='My Exp', max_length=5000),
        ),
    ]
