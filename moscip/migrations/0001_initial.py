# Generated by Django 5.0.2 on 2024-03-02 19:52

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BadgeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BadgeTypePoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_points', models.IntegerField(default=0)),
                ('date', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('duration', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EventOrganisers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Patrol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('colour', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Scout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('ssa_id', models.CharField(max_length=200)),
                ('dob', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Troop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
                ('badge_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='moscip.badgetype')),
            ],
        ),
        migrations.AddField(
            model_name='badgetype',
            name='points',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='moscip.badgetypepoints'),
        ),
        migrations.CreateModel(
            name='PatrolMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.datetime.now)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('rank', models.CharField(blank=True, max_length=200, null=True)),
                ('patrol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='moscip.patrol')),
                ('scout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patrols', to='moscip.scout')),
            ],
        ),
        migrations.CreateModel(
            name='ScoutBadge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_awarded', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scouts', to='moscip.badge')),
                ('scout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='badges', to='moscip.patrolmember')),
            ],
        ),
    ]
