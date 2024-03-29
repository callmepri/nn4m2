# Generated by Django 4.1.5 on 2023-11-22 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_alter_successfulstudent_university'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success_rate', models.IntegerField()),
                ('success_amount', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='successfulstudent',
            name='university',
            field=models.CharField(choices=[('empty.png', 'Empty'), ('unsw-logo.png', 'University of New South Wales'), ('wsu-logo.webp', 'Western Sydney University'), ('griffith-logo.png', 'Griffith University'), ('une-logo.png', 'University of New England'), ('charles-stuart-logo.png', 'Charles Stuart'), ('anu-logo.png', 'Australian National University'), ('university-of-qld-logo.png', 'University of Queensland'), ('university-of-adelaide-logo.png', 'University of Adelaide')], max_length=100),
        ),
    ]
