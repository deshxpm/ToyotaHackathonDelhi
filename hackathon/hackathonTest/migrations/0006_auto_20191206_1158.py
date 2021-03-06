# Generated by Django 3.0 on 2019-12-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathonTest', '0005_auto_20191206_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionQuiz',
            fields=[
                ('qId', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('A', models.CharField(max_length=1000)),
                ('B', models.CharField(max_length=1000)),
                ('C', models.CharField(max_length=1000)),
                ('D', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='qId',
        ),
        migrations.AddField(
            model_name='question',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
