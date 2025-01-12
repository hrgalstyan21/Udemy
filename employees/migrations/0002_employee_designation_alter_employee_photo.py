# Generated by Django 5.1.4 on 2025-01-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(default='Unspecified', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to='images11'),
        ),
    ]
