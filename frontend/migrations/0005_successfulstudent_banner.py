# Generated by Django 4.1.5 on 2023-11-22 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_alter_successfulstudent_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='successfulstudent',
            name='banner',
            field=models.BooleanField(default=False),
        ),
    ]