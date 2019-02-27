# Generated by Django 2.1 on 2018-11-13 16:18

from django.db import migrations

def fill_progress(apps, schema_editor):
    ValidationRun = apps.get_model('validator', 'ValidationRun')
    
    for run in ValidationRun.objects.all():
        if (run.progress == 0) and (run.end_time is not None):
            run.progress = 100
            run.save()
        
class Migration(migrations.Migration):

    dependencies = [
        ('validator', '0010_auto_20181030_1158'),
    ]

    operations = [
        migrations.RunPython(fill_progress),
    ]
