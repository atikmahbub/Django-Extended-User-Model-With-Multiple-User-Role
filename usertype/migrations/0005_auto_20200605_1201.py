# Generated by Django 3.0.7 on 2020-06-05 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usertype', '0004_auto_20200605_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Phone_Number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
