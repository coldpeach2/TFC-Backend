# Generated by Django 4.1 on 2022-11-30 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0009_alter_classes_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='frequency',
            field=models.IntegerField(choices=[(1, 'Daily'), (3, 'Monthly'), (0, 'Once'), (2, 'Weekly')], null=True),
        ),
    ]