# Generated by Django 4.1.6 on 2023-03-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0036_past_appoint_treatment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile', models.CharField(default='null', max_length=100)),
                ('doctor', models.CharField(default='null', max_length=100)),
                ('session', models.CharField(default='1', max_length=100)),
                ('treat', models.CharField(default='null', max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='past_appoint',
            name='session',
        ),
        migrations.RemoveField(
            model_name='past_appoint',
            name='treatment',
        ),
    ]
