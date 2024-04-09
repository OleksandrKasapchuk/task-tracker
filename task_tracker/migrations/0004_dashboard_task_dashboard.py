# Generated by Django 5.0.4 on 2024-04-06 23:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0003_remove_task_start_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='dashboard',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='task_tracker.dashboard'),
            preserve_default=False,
        ),
    ]
