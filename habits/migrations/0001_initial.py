# Generated by Django 5.0.6 on 2024-07-11 10:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('action', models.CharField(max_length=100)),
                ('pleasant_habit', models.BooleanField(default=False)),
                ('periodicity', models.CharField(default='daily', max_length=100)),
                ('reward', models.CharField(max_length=100)),
                ('time_required', models.DurationField()),
                ('public', models.BooleanField(default=False)),
                ('execution_time', models.DateTimeField(blank=True, null=True)),
                ('linked_habit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='linked_habits', to='habits.habit')),
                ('related_habit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_habits', to='habits.habit')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='habits', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_edit_habit', 'Can edit habit'), ('can_delete_habit', 'Can delete habit')),
            },
        ),
    ]
