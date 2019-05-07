# Generated by Django 2.1 on 2018-09-21 14:56

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('organisation', models.CharField(blank=True, max_length=30)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ValidationRun',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(verbose_name='started')),
                ('end_time', models.DateTimeField(null=True, verbose_name='finished')),
                ('total_points', models.IntegerField(default=0)),
                ('error_points', models.IntegerField(default=0)),
                ('ok_points', models.IntegerField(default=0)),
                ('data_dataset', models.CharField(choices=[('C3S', 'C3S'), ('ISMN', 'ISMN'), ('GLDAS', 'GLDAS'), ('SMAP', 'SMAP')], default='C3S', max_length=10)),
                ('data_version', models.CharField(choices=[('v201706', 'v201706'), ('v201801', 'v201801'), ('v20180712_USA', '20180712 USA'), ('v20180712_TEST', '20180712 testset'), ('v20180712_MINI', '20180712 mini testset'), ('V20180830_GLOBAL', '20180830 global'), ('v5_PM', 'v5 PM/ascending'), ('GLDAS_NOAH025_3H.2.1', 'NOAH025 3H.2.1')], default='v201706', max_length=20)),
                ('data_variable', models.CharField(choices=[('sm', 'sm'), ('soil moisture', 'soil moisture'), ('soil_moisture', 'soil_moisture'), ('SoilMoi0_10cm_inst', 'SoilMoi0_10cm_inst')], default='sm', max_length=20)),
                ('ref_dataset', models.CharField(choices=[('C3S', 'C3S'), ('ISMN', 'ISMN'), ('GLDAS', 'GLDAS'), ('SMAP', 'SMAP')], default='ISMN', max_length=10)),
                ('ref_version', models.CharField(choices=[('v201706', 'v201706'), ('v201801', 'v201801'), ('v20180712_USA', '20180712 USA'), ('v20180712_TEST', '20180712 testset'), ('v20180712_MINI', '20180712 mini testset'), ('V20180830_GLOBAL', '20180830 global'), ('v5_PM', 'v5 PM/ascending'), ('GLDAS_NOAH025_3H.2.1', 'NOAH025 3H.2.1')], default='v20180712_MINI', max_length=20)),
                ('ref_variable', models.CharField(choices=[('sm', 'sm'), ('soil moisture', 'soil moisture'), ('soil_moisture', 'soil_moisture'), ('SoilMoi0_10cm_inst', 'SoilMoi0_10cm_inst')], default='soil moisture', max_length=20)),
                ('scaling_ref', models.CharField(choices=[('data', 'data to reference'), ('ref', 'reference to data')], default='ref', max_length=4)),
                ('scaling_method', models.CharField(choices=[('min_max', 'Min/Max'), ('linreg', 'Linear regression'), ('mean_std', 'Mean/standard deviation'), ('lin_cdf_match', 'CDF matching with linear interpolation'), ('cdf_match', 'CDF matching with 5-th order spline fitting')], default='mean_std', max_length=20)),
                ('interval_from', models.DateTimeField(null=True)),
                ('interval_to', models.DateTimeField(null=True)),
                ('output_file', models.FileField(null=True, upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]