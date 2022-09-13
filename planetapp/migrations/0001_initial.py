# Generated by Django 4.0.6 on 2022-08-22 04:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City_event',
            fields=[
                ('event_id', models.IntegerField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=10)),
                ('question', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('programe_name', models.CharField(max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('feedback_text', models.TextField()),
                ('rating', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JobDescription',
            fields=[
                ('job_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('post_name', models.CharField(max_length=30)),
                ('no_of_seat', models.IntegerField()),
                ('last_apply', models.DateField()),
                ('post_date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Parent_detail',
            fields=[
                ('id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Program_detail',
            fields=[
                ('program_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('duration', models.CharField(max_length=20)),
                ('fees', models.CharField(max_length=30)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('age_group', models.CharField(max_length=20)),
            ],
        ),
    ]