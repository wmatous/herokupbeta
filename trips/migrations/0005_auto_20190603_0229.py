# Generated by Django 2.2.1 on 2019-06-03 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_auto_20190603_0209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='LAYERS',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='MARKERS',
        ),
        migrations.AddField(
            model_name='layer',
            name='TRIP',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LAYERS', to='trips.Trip'),
        ),
        migrations.AddField(
            model_name='marker',
            name='TRIP',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MARKERS', to='trips.Trip'),
        ),
    ]
