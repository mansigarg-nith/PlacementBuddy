# Generated by Django 4.1.2 on 2022-11-07 17:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_experience_anonymity_experience_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='exp',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
