# Generated by Django 3.1.6 on 2021-11-16 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=200)),
                ('capacity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='test_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('identification', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('auth', models.CharField(choices=[('U', 'User'), ('A', 'Admin')], max_length=1)),
                ('sites', models.ManyToManyField(to='app_manage.Site')),
            ],
        ),
    ]
