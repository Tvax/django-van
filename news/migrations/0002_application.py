# Generated by Django 2.1.1 on 2018-09-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to='applications/')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
