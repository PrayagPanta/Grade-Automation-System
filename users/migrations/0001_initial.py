# Generated by Django 3.0.1 on 2020-02-11 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('role', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher')], default='S', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('Sid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.Profile')),
                ('Name', models.CharField(max_length=30)),
                ('School', models.CharField(max_length=80)),
                ('Exam_Center', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('Tid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.Profile')),
                ('Name', models.CharField(max_length=30)),
                ('School', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('Sid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.StudentInfo')),
                ('Complaint', models.CharField(max_length=500)),
            ],
        ),
    ]
