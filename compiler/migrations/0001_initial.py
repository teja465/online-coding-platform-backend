# Generated by Django 3.2.2 on 2021-05-14 07:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='problem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('statement', models.TextField(max_length=5000)),
                ('title', models.CharField(max_length=200)),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=15)),
                ('constraints', models.TextField(max_length=200)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='test_case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.CharField(max_length=100)),
                ('output', models.CharField(max_length=500)),
                ('description', models.TextField(default='', max_length=500)),
                ('isPublic', models.BooleanField(default=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compiler.problem')),
            ],
        ),
    ]
