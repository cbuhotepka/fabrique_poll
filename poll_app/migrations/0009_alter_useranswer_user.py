# Generated by Django 3.2.4 on 2021-06-28 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0008_alter_useranswer_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_of_user', to='poll_app.user'),
        ),
    ]
