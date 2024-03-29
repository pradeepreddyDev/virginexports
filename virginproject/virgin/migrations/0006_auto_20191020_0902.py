# Generated by Django 2.2.6 on 2019-10-20 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virgin', '0005_auto_20191020_0843'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'projects category', 'verbose_name_plural': 'projects category'},
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='virgin.Category')),
            ],
            options={
                'verbose_name': 'projects',
                'verbose_name_plural': 'projects',
                'db_table': 'projects',
            },
        ),
    ]
