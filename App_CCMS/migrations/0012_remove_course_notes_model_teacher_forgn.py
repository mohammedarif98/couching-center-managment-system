# Generated by Django 4.1 on 2022-08-10 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_CCMS', '0011_course_notes_model_user_course_note_forgn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_notes_model',
            name='Teacher_Forgn',
        ),
    ]
