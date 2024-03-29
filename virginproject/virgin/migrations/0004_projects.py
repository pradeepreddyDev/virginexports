# Generated by Django 2.2.6 on 2019-10-20 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virgin', '0003_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projects_title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'projects',
                'verbose_name_plural': 'projects',
                'db_table': 'projects',
            },
        ),
    ]
