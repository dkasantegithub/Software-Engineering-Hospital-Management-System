# Generated by Django 3.0.7 on 2020-06-21 16:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20200615_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_record',
            name='check_in',
        ),
        migrations.RemoveField(
            model_name='patient_record',
            name='check_out',
        ),
        migrations.AddField(
            model_name='patient_record',
            name='check_in_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_record',
            name='check_in_period',
            field=models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening'), ('night', 'Night')], default=django.utils.timezone.now, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_record',
            name='check_out_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_record',
            name='check_out_period',
            field=models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening'), ('night', 'Night')], default=django.utils.timezone.now, max_length=64),
            preserve_default=False,
        ),
    ]