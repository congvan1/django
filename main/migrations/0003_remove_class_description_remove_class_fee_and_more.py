# Generated by Django 4.1.3 on 2022-11-29 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='description',
        ),
        migrations.RemoveField(
            model_name='class',
            name='fee',
        ),
        migrations.RemoveField(
            model_name='class',
            name='is_valid',
        ),
        migrations.RemoveField(
            model_name='class',
            name='level',
        ),
        migrations.RemoveField(
            model_name='class',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='address',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='age',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='image_license',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='license',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
    ]
