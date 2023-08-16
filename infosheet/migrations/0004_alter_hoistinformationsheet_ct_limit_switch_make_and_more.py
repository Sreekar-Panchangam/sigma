# Generated by Django 4.2.4 on 2023-08-16 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("infosheet", "0003_hoistinformationsheet_proof_of_load_applied"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hoistinformationsheet",
            name="ct_limit_switch_make",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="hoistinformationsheet",
            name="ct_limit_switch_serial_number",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="hoistinformationsheet",
            name="ct_limit_switch_type",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="hoistinformationsheet",
            name="hoisting_limit_switch_make",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="hoistinformationsheet",
            name="hoisting_limit_switch_serial_number",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="hoistinformationsheet",
            name="hoisting_limit_switch_type",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
