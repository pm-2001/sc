# Generated by Django 3.0.5 on 2021-10-16 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_question_people_who_answered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='people_who_answered',
        ),
    ]
