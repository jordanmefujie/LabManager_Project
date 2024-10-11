# Generated by Django 5.0.7 on 2024-10-10 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('services_offered', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Laboratory',
                'verbose_name_plural': 'Laboratories',
                'ordering': ['name'],
            },
        ),
    ]
