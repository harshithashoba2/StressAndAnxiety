# Generated by Django 4.1.6 on 2023-04-02 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0045_severity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greetings', models.CharField(max_length=100)),
                ('readiness', models.CharField(max_length=100)),
                ('ques1', models.CharField(max_length=4)),
                ('ques2', models.CharField(max_length=4)),
                ('ques3', models.CharField(max_length=4)),
                ('ques4', models.CharField(max_length=4)),
                ('ques5', models.CharField(max_length=4)),
                ('ques6', models.CharField(max_length=4)),
                ('ques7', models.CharField(max_length=4)),
                ('ques8', models.CharField(max_length=4)),
                ('ques9', models.CharField(max_length=4)),
                ('ques10', models.CharField(max_length=4)),
                ('ques11', models.CharField(max_length=4)),
                ('ques12', models.CharField(max_length=4)),
                ('ques13', models.CharField(max_length=4)),
                ('ques14', models.CharField(max_length=4)),
                ('ques15', models.CharField(max_length=4)),
                ('ques16', models.CharField(max_length=4)),
                ('ques17', models.CharField(max_length=4)),
                ('ques18', models.CharField(max_length=4)),
                ('ques19', models.CharField(max_length=4)),
                ('ques20', models.CharField(max_length=4)),
                ('ques21', models.CharField(max_length=4)),
                ('ques22', models.CharField(max_length=4)),
                ('stress', models.CharField(max_length=4)),
                ('anxiety', models.CharField(max_length=4)),
                ('Profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='detection.profile')),
            ],
        ),
    ]
