# Generated by Django 4.1.3 on 2023-08-12 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ('-dete_created',)},
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
