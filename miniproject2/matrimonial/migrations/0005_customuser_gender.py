# Generated by Django 5.1.3 on 2024-12-03 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonial', '0004_alter_friendrequest_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=15),
        ),
    ]
