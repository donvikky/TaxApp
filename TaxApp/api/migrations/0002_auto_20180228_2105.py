# Generated by Django 2.0.2 on 2018-02-28 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taxpayer',
            options={'ordering': ('-created_at',), 'verbose_name': 'Individual Tax Payer'},
        ),
        migrations.AlterField(
            model_name='companyaddress',
            name='ward',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='Ward'),
        ),
        migrations.AlterField(
            model_name='companyaddressauditlogentry',
            name='ward',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='Ward'),
        ),
        migrations.AlterField(
            model_name='residentialaddress',
            name='ward',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='Ward'),
        ),
        migrations.AlterField(
            model_name='residentialaddressauditlogentry',
            name='ward',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='Ward'),
        ),
        migrations.AlterField(
            model_name='taxpayer',
            name='other_name',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='Other Name'),
        ),
        migrations.AlterField(
            model_name='taxpayerauditlogentry',
            name='other_name',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='Other Name'),
        ),
    ]