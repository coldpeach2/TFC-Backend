# Generated by Django 4.1 on 2022-11-29 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_subscription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='subscription_choices',
            field=models.CharField(choices=[('14.99/month', '14.99/month'), ('149.99/year', '149.99/year'), ('Free', 'Free')], default='Free', max_length=120),
        ),
    ]