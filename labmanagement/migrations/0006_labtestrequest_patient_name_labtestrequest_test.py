# Generated by Django 5.0.7 on 2024-09-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labmanagement', '0005_labreport_labresult_labresultverification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtestrequest',
            name='patient_name',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='labtestrequest',
            name='test',
            field=models.CharField(default='Unknown Test', max_length=255),
        ),
    ]
