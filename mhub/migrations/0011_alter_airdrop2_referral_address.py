# Generated by Django 4.1.3 on 2023-06-23 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhub', '0010_airdrop2_delete_airdrop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airdrop2',
            name='referral_address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
