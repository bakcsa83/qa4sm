# Generated by Django 2.1 on 2018-11-30 10:15

from django.db import migrations

def convert_datasets(apps, schema_editor):

    # class variables copied from (old) ValidationRun class:

    ## datasets
    C3S = 'C3S'
    ISMN = 'ISMN'
    GLDAS = 'GLDAS'
    SMAP = 'SMAP'
    ASCAT = 'ASCAT'

    REF_DATASETS = (
        (ISMN, 'ISMN'),
        (GLDAS, 'GLDAS'),
        )

    DATA_DATASETS = (
        (C3S, 'C3S'),
        (SMAP, 'SMAP level 3'),
        (ASCAT, 'H-SAF ASCAT SSM CDR')
        )

    DATASETS = DATA_DATASETS + REF_DATASETS

    ## dataset versions
    C3S_V201706 = 'v201706'
    ISMN_V20180712_TEST = 'v20180712_TEST'
    ISMN_V20180712_MINI = 'v20180712_MINI'
    ISMN_V20180830_GLOBAL = 'V20180830_GLOBAL'
    SMAP_V5_PM = 'v5_PM'
    GLDAS_V2_1 = 'GLDAS_NOAH025_3H.2.1'
    GLDAS_TEST = 'GLDAS_TEST'
    ASCAT_H113 = 'H113'

    VERSIONS = (
        (C3S, (
            (C3S_V201706, 'v201706'),
            )
        ),
        (ISMN, (
            (ISMN_V20180712_TEST, '20180712 testset'),
            (ISMN_V20180712_MINI, '20180712 mini testset'),
            (ISMN_V20180830_GLOBAL, '20180830 global'),
            )
        ),
        (SMAP, (
            (SMAP_V5_PM, 'v5 PM/ascending'),
            )
        ),
        (GLDAS, (
            (GLDAS_V2_1, 'NOAH025 3H.2.1'),
            (GLDAS_TEST, 'TEST'),
            )
        ),
        (ASCAT, (
            (ASCAT_H113, 'H113'),
            )
        ),
        )

    ## dataset data variables
    VAR_SM = 'sm'
    VAR_SOILMOISTURE = 'soil moisture'
    VAR_SOIL_MOISTURE = 'soil_moisture'
    VAR_SOIL_MOI_0_10CM = 'SoilMoi0_10cm_inst'
    VAR_SOIL_MOI_10_40CM = 'SoilMoi10_40cm_inst'
    VAR_SOIL_MOI_40_100CM = 'SoilMoi40_100cm_inst'
    VAR_SOIL_MOI_100_200CM = 'SoilMoi100_200cm_inst'

    DATA_VARIABLES = (
        (ISMN, (
            (VAR_SOILMOISTURE,'soil moisture'),
            )
         ),
        (C3S, (
            (VAR_SM, 'sm'),
            )
        ),
        (SMAP, (
            (VAR_SOIL_MOISTURE, 'soil_moisture'),
            )
        ),
        (GLDAS, (
            (VAR_SOIL_MOI_0_10CM, 'SoilMoi0_10cm_inst'),
            (VAR_SOIL_MOI_10_40CM, 'SoilMoi10_40cm_inst'),
            (VAR_SOIL_MOI_40_100CM, 'SoilMoi40_100cm_inst'),
            (VAR_SOIL_MOI_100_200CM, 'SoilMoi100_200cm_inst'),
            )
        ),
        (ASCAT, (
            (VAR_SM, 'sm'),
            )
        ),
        )

    # now put the contents of those variables into the database

    Dataset = apps.get_model('validator', 'Dataset')
    DataVariable = apps.get_model('validator', 'DataVariable')
    DatasetVersion = apps.get_model('validator', 'DatasetVersion')
    DataFilter = apps.get_model('validator', 'DataFilter')

    version_dict = dict(VERSIONS)
    variable_dict = dict(DATA_VARIABLES)

    filter_dict = { # you can OR together query sets with the | operator
                   ISMN: DataFilter.objects.filter(name='FIL_ALL_VALID_RANGE') | DataFilter.objects.filter(name__startswith='FIL_ISMN_'),
                   C3S: DataFilter.objects.filter(name='FIL_ALL_VALID_RANGE') | DataFilter.objects.filter(name__startswith='FIL_C3S_'),
                   SMAP: DataFilter.objects.filter(name='FIL_ALL_VALID_RANGE'),
                   GLDAS: DataFilter.objects.filter(name='FIL_ALL_VALID_RANGE') | DataFilter.objects.filter(name__startswith='FIL_GLDAS'),
                   ASCAT: DataFilter.objects.filter(name='FIL_ALL_VALID_RANGE') | DataFilter.objects.filter(name__startswith='FIL_ASCAT'),
                   }

    for names in DATASETS:
        dataset_name = names[0]
        # create dataset
        d = Dataset()
        d.short_name = dataset_name
        d.pretty_name = names[1]
        d.is_reference = names in REF_DATASETS
        d.save()

        # create versions
        for s, p in version_dict[dataset_name]:
            v = DatasetVersion()
            if dataset_name != GLDAS:
                v.short_name = dataset_name + "_" + s.upper()
            else:
                v.short_name = dataset_name + "_" + p.upper().replace(' ', '_').replace('.', '_')
            v.pretty_name = p
            v.save()
            d.versions.add(v)

        # create variables
        for s, p in variable_dict[dataset_name]:
            lower_bound = 0
            upper_bound = 1
            if (dataset_name == ASCAT):
                upper_bound = 100

            if (dataset_name == GLDAS):
                upper_bound = None
                if s == VAR_SOIL_MOI_0_10CM:
                    upper_bound = 100
                if s == VAR_SOIL_MOI_10_40CM:
                    upper_bound = 300
                if s == VAR_SOIL_MOI_40_100CM:
                    upper_bound = 600
                if s == VAR_SOIL_MOI_100_200CM:
                    upper_bound = 1000

            v = DataVariable()
            v.short_name = dataset_name + "_" + s.replace(' ', '_')
            v.pretty_name = p
            v.min_value = lower_bound
            v.max_value = upper_bound
            v.save()
            d.variables.add(v)

        # add filters
        for f in filter_dict[dataset_name]:
            d.filters.add(f)

class Migration(migrations.Migration):

    dependencies = [
        ('validator', '0016_auto_20181130_1538'),
    ]

    operations = [
        migrations.RunPython(convert_datasets),
    ]