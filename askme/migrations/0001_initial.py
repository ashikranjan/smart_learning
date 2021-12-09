# Generated by Django 3.2.10 on 2021-12-09 11:16

from django.db import migrations, models
import django.db.models.deletion
import storage_backends


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentQuery',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('query', models.TextField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('student_id', models.IntegerField(default=0)),
                ('mentor_id', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QueryDocuments',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('document_url', models.FileField(default='defaultprofilepic.png', storage=storage_backends.PublicMediaStorage(), upload_to='')),
                ('query_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='askme.studentquery')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]