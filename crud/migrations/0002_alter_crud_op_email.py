# Generated by Django 3.2 on 2021-04-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud_op',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
