# Generated by Django 4.2.5 on 2023-12-06 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bittu', '0002_alter_contact_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='PhoneNumber',
            field=models.CharField(max_length=122),
        ),
    ]
