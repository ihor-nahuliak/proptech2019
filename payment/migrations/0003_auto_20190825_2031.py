# Generated by Django 2.2.4 on 2019-08-25 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20190825_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c2bpayment',
            name='TransTime',
            field=models.DateTimeField(),
        ),
    ]
