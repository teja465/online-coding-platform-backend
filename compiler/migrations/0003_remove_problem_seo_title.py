# Generated by Django 3.2.2 on 2021-05-14 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compiler', '0002_problem_seo_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='seo_title',
        ),
    ]
