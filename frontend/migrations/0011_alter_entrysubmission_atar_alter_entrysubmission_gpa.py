# Generated by Django 4.1.5 on 2023-12-17 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0010_alter_entrysubmission_atar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrysubmission',
            name='atar',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='entrysubmission',
            name='gpa',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]