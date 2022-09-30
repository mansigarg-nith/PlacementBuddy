# Generated by Django 3.2.8 on 2022-09-30 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drive', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(choices=[('1', 'Easy'), ('2', 'Medium'), ('3', 'Hard')], default='1', max_length=6)),
                ('verdict', models.BooleanField()),
                ('drive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drive.drive')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
