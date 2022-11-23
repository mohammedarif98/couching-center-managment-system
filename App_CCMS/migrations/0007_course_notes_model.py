# Generated by Django 4.1 on 2022-08-09 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_CCMS', '0006_teacher_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Notes_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Discription', models.CharField(max_length=3000)),
                ('Bg_Image', models.ImageField(upload_to='image/')),
                ('PDF_Note', models.FileField(blank=True, null=True, upload_to='document/')),
                ('Course_Forgn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App_CCMS.course_model')),
                ('Teacher_Forgn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App_CCMS.teacher_model')),
            ],
        ),
    ]
