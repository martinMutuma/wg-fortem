# Generated by Django 2.2.1 on 2019-06-18 07:19

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wger.utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0004_auto_20190606_1132'),
        ('core', '0004_daysofweek_workout_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='A description of what is done on this day (e.g. "Pull day") or what body parts are trained (e.g. "Arms and abs")', max_length=100, verbose_name='Description')),
                ('day', models.ManyToManyField(to='core.DaysOfWeek', verbose_name='Day')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Name or short description of the schedule. For example 'Program XYZ'.", max_length=100, verbose_name='Name')),
                ('start_date', wger.utils.fields.Html5DateField(default=datetime.date.today, verbose_name='Start date')),
                ('is_active', models.BooleanField(default=True, help_text='Tick the box if you want to mark this schedule as your active one (will be shown e.g. on your dashboard). All other schedules will then be marked as inactive', verbose_name='Schedule active')),
                ('is_loop', models.BooleanField(default=False, help_text='Tick the box if you want to repeat the schedules in a loop (i.e. A, B, C, A, B, C, and so on)', verbose_name='Is a loop')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Order')),
                ('sets', models.IntegerField(default=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Number of sets')),
                ('exerciseday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Day', verbose_name='Exercise day')),
                ('exercises', models.ManyToManyField(to='exercises.Exercise', verbose_name='Exercises')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('comment', models.CharField(blank=True, help_text="A short description or goal of the workout. For example 'Focus on back' or 'Week 1 of program xy'.", max_length=100, verbose_name='Description')),
                ('cycle_type', models.CharField(choices=[('Microcycle', 'Microcycle - one week plan'), ('Mesocycle', 'Mesocycle - Two to six weeks plan'), ('Macrocycle', 'Macrocycle - one year plan')], default='', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='WorkoutLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Repetitions')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Weight')),
                ('date', wger.utils.fields.Html5DateField(verbose_name='Date')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.Exercise', verbose_name='Exercise')),
                ('repetition_unit', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.RepetitionUnit', verbose_name='Unit')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('weight_unit', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.WeightUnit', verbose_name='Unit')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Workout', verbose_name='Workout')),
            ],
            options={
                'ordering': ['date', 'reps'],
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(600)], verbose_name='Amount')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1500)], verbose_name='Weight')),
                ('order', models.IntegerField(blank=True, verbose_name='Order')),
                ('comment', models.CharField(blank=True, max_length=100, verbose_name='Comment')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.Exercise', verbose_name='Exercises')),
                ('repetition_unit', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.RepetitionUnit', verbose_name='Unit')),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Set', verbose_name='Sets')),
                ('weight_unit', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.WeightUnit', verbose_name='Unit')),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='ScheduleStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(default=4, help_text='The duration in weeks', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(25)], verbose_name='Duration')),
                ('order', models.IntegerField(default=1, verbose_name='Order')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Schedule', verbose_name='schedule')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Workout')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='day',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Workout', verbose_name='Workout'),
        ),
        migrations.CreateModel(
            name='WorkoutSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', wger.utils.fields.Html5DateField(verbose_name='Date')),
                ('notes', models.TextField(blank=True, help_text='Any notes you might want to save about this workout session.', null=True, verbose_name='Notes')),
                ('impression', models.CharField(choices=[('1', 'Bad'), ('2', 'Neutral'), ('3', 'Good')], default='2', help_text='Your impression about this workout session. Did you exercise as well as you could?', max_length=2, verbose_name='General impression')),
                ('time_start', models.TimeField(blank=True, null=True, verbose_name='Start time')),
                ('time_end', models.TimeField(blank=True, null=True, verbose_name='Finish time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Workout', verbose_name='Workout')),
            ],
            options={
                'ordering': ['date'],
                'unique_together': {('date', 'user')},
            },
        ),
    ]
