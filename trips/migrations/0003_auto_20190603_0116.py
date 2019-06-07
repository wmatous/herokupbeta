# Generated by Django 2.2.1 on 2019-06-03 01:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_auto_20190601_0313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forecast',
            name='id',
        ),
        migrations.RemoveField(
            model_name='layer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='marker',
            name='id',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='id',
        ),
        migrations.AddField(
            model_name='forecast',
            name='ID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='layer',
            name='ID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='marker',
            name='ID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='trip',
            name='ID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]