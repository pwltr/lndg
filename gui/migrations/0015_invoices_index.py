# Generated by Django 3.2.7 on 2021-12-26 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0014_failedhtlcs'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoices',
            name='index',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
