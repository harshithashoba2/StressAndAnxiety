# Generated by Django 4.1.6 on 2023-03-30 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0031_past_appoint_problem_update_appoint_problem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans1', models.CharField(max_length=100)),
                ('ans2', models.CharField(max_length=100)),
                ('ans3', models.CharField(max_length=100)),
                ('ans4', models.CharField(max_length=100)),
                ('ans5', models.CharField(max_length=100)),
                ('ans6', models.CharField(max_length=100)),
                ('ans7', models.CharField(max_length=100)),
                ('ans8', models.CharField(max_length=100)),
                ('ans9', models.CharField(max_length=100)),
                ('ans10', models.CharField(max_length=100)),
                ('ans11', models.CharField(max_length=100)),
                ('ans12', models.CharField(max_length=100)),
                ('ans13', models.CharField(max_length=100)),
                ('ans14', models.CharField(max_length=100)),
                ('ans15', models.CharField(max_length=100)),
                ('ans16', models.CharField(max_length=100)),
                ('ans17', models.CharField(max_length=100)),
                ('ans18', models.CharField(max_length=100)),
                ('ans19', models.CharField(max_length=100)),
                ('ans20', models.CharField(max_length=100)),
                ('Profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='detection.profile')),
            ],
        ),
    ]
