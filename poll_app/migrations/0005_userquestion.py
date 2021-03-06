# Generated by Django 3.2.4 on 2021-06-28 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0004_rename_satrt_date_question_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.CharField(max_length=1024)),
                ('answer', models.ManyToManyField(to='poll_app.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll_app.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll_app.user')),
            ],
        ),
    ]
