# Generated by Django 4.1.2 on 2022-10-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(max_length=500)),
                ('imageType', models.CharField(choices=[('1', 'Type 1'), ('2', 'Type 2'), ('3', 'Type 3')], default='1', max_length=1)),
                ('city', models.CharField(blank=True, max_length=64, null=True)),
                ('state', models.CharField(blank=True, max_length=64, null=True)),
                ('country', models.CharField(blank=True, max_length=64, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('timeStamp', models.DateTimeField()),
            ],
        ),
    ]