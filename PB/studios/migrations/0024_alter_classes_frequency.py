# Generated by Django 4.1 on 2022-11-30 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0023_alter_classes_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='frequency',
            field=models.IntegerField(choices=[(0, 'Once'), (1, 'Daily'), (2, 'Weekly'), (3, 'Monthly')], null=True),
        ),
    ]