# Generated by Django 4.0.6 on 2022-08-03 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Foodbolapp', '0004_alter_club_yil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='davlat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='davlat_clublari', to='Foodbolapp.davlat'),
        ),
    ]