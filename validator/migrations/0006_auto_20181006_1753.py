# Generated by Django 2.1 on 2018-10-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validator', '0005_auto_20181006_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='validationrun',
            name='data_filters',
            field=models.ManyToManyField(related_name='data_filters', to='validator.DataFilter'),
        ),
        migrations.AddField(
            model_name='validationrun',
            name='ref_filters',
            field=models.ManyToManyField(related_name='ref_filters', to='validator.DataFilter'),
        ),
    ]
