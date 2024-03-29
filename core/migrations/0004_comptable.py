# Generated by Django 5.0.2 on 2024-02-29 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_col1_datatable_car_rename_col2_datatable_data_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outscan_Performance', models.CharField(blank=True, max_length=100, null=True)),
                ('eds_rvp_conversion', models.CharField(blank=True, max_length=100, null=True)),
                ('service_center', models.CharField(blank=True, max_length=100, null=True)),
                ('fresh', models.CharField(blank=True, max_length=100, null=True)),
                ('overall_conversion', models.CharField(blank=True, max_length=100, null=True)),
                ('rvp_done', models.CharField(blank=True, max_length=100, null=True)),
                ('eds', models.CharField(blank=True, max_length=100, null=True)),
                ('eds_conversion', models.CharField(blank=True, max_length=100, null=True)),
                ('rvp', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
