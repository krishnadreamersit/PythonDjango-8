# Generated by Django 4.0.5 on 2022-07-21 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app3_1', '0002_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='fullnane',
            new_name='fullname',
        ),
    ]
