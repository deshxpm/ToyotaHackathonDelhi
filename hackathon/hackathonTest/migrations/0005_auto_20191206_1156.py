# Generated by Django 3.0 on 2019-12-06 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathonTest', '0004_remove_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.AddField(
            model_name='question',
            name='qId',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
