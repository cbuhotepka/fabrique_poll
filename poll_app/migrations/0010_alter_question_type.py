# Generated by Django 3.2.4 on 2021-06-28 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0009_alter_useranswer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('single', 'Single choice'), ('multiple', 'Multiple choice'), ('text', 'Text answer')], max_length=32),
        ),
    ]
