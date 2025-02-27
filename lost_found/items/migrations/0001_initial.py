# Generated by Django 5.1.4 on 2024-12-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoundItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('contact_number', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=200)),
                ('date_found', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='found_items/')),
            ],
        ),
        migrations.CreateModel(
            name='LostItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('date_lost', models.DateField()),
                ('contact_number', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='lost_and_found_images/')),
            ],
        ),
    ]
