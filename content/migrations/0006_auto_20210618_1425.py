# Generated by Django 3.1.7 on 2021-06-18 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0012_userplace'),
        ('content', '0005_cimagess_userplaces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userplaces',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='place.category'),
        ),
    ]