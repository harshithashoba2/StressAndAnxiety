# Generated by Django 4.1.6 on 2023-03-05 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0010_alter_result_stage0_alter_result_stage1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='acute',
            name='Profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='detection.profile'),
        ),
        migrations.AddField(
            model_name='acute_ans',
            name='Profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='detection.profile'),
        ),
        migrations.AddField(
            model_name='gad',
            name='Profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='detection.profile'),
        ),
        migrations.AddField(
            model_name='gad_ans',
            name='Profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='detection.profile'),
        ),
        migrations.AddField(
            model_name='panic',
            name='Profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='detection.profile'),
        ),
        migrations.AddField(
            model_name='panic_ans',
            name='Profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='detection.profile'),
        ),
        migrations.AddField(
            model_name='ptsd',
            name='Profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='detection.profile'),
        ),
        migrations.AddField(
            model_name='ptsd_ans',
            name='Profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='detection.profile'),
        ),
    ]
