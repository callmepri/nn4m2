# Generated by Django 4.2.3 on 2023-07-22 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_successfulstudent_percentile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successfulstudent',
            name='university',
            field=models.CharField(choices=[('unsw-logo.png', 'University of New South Wales'), ('wsu-logo.webp', 'Western Sydney University'), ('griffith-logo.png', 'Griffith University'), ('une-logo.png', 'University of New England'), ('charles-stuart-logo.png', 'Charles Stuart'), ('anu-logo.png', 'Australian National University'), ('university-of-qld-logo.png', 'University of Queensland')], max_length=100),
        ),
    ]
