# Generated by Django 4.1 on 2022-11-30 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0014_alter_classes_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='frequency',
            field=models.IntegerField(choices=[(3, 'Monthly'), (1, 'Daily'), (0, 'Once'), (2, 'Weekly')], null=True),
        ),
    ]