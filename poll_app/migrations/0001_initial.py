# Generated by Django 3.2.4 on 2021-06-28 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=4096)),
                ('type', models.CharField(choices=[('s', 'Single choice'), ('m', 'Multiple choice'), ('t', 'Text answer')], max_length=1)),
                ('satrt_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=1024)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll_app.question')),
            ],
        ),
    ]
