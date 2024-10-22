# Generated by Django 5.0.4 on 2024-04-04 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aadhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=100)),
                ('stu_email', models.CharField(max_length=100)),
                ('stu_contact', models.CharField(max_length=200)),
                ('aadhar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.aadhar')),
            ],
        ),
    ]
