# Generated by Django 4.1.6 on 2023-03-14 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0016_alter_result_stage0_alter_result_stage1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage0', models.CharField(default='null', max_length=5000, null=True)),
                ('stage1', models.CharField(default='null', max_length=5000, null=True)),
                ('stage2', models.CharField(default='null', max_length=5000, null=True)),
                ('stage3', models.CharField(default='null', max_length=5000, null=True)),
                ('risk', models.CharField(default='null', max_length=100)),
                ('Profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='detection.profile')),
            ],
        ),
    ]