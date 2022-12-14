# Generated by Django 4.1 on 2022-09-20 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateLead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('notes', models.TextField()),
                ('received', models.DateTimeField(verbose_name='Date Received')),
            ],
            options={
                'verbose_name_plural': 'Created Leads',
            },
        ),
        migrations.AlterModelOptions(
            name='lead',
            options={'verbose_name_plural': 'Leads'},
        ),
    ]
