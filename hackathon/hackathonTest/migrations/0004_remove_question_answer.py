# Generated by Django 3.0 on 2019-12-06 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackathonTest', '0003_answer_a11'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
    ]