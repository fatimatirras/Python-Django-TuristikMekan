# Generated by Django 3.1.7 on 2021-03-31 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210331_0444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='orderno',
        ),
    ]
