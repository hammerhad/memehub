# Generated by Django 4.1.3 on 2023-06-21 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhub', '0007_alter_smartcontract_isclaimingenabled'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airdrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claimed', models.BooleanField()),
                ('referral', models.CharField(max_length=100)),
            ],
        ),
    ]
