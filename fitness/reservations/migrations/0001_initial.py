# Generated by Django 4.2.1 on 2023-05-08 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=30)),
                ('year_of_production', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('town', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('entry', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('difficulty', models.CharField(max_length=100)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.equipment')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateField()),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.gym')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.user')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.workout')),
            ],
        ),
    ]
