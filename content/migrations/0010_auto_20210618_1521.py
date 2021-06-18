# Generated by Django 3.1.7 on 2021-06-18 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_userplaces_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userplaces',
            name='parent',
        ),
        migrations.AddField(
            model_name='userplaces',
            name='menu',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.menu'),
        ),
    ]