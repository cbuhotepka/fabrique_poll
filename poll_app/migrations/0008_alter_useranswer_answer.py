# Generated by Django 3.2.4 on 2021-06-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0007_auto_20210628_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='answer',
            field=models.ManyToManyField(blank=True, to='poll_app.Answer'),
        ),
    ]