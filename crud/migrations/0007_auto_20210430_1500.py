# Generated by Django 3.1.7 on 2021-04-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_alter_emp_details_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp_details',
            name='technology',
            field=models.CharField(max_length=300),
        ),
    ]