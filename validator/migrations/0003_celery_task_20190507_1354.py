# Generated by Django 2.2 on 2019-05-07 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('validator', '0002_change_celery_task_id_20190327_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celerytask',
            name='validation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='celery_tasks', to='validator.ValidationRun'),
        ),
    ]