# Generated by Django 5.1.3 on 2024-12-02 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonial', '0003_friendrequest'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friendrequest',
            unique_together={('sender', 'receiver')},
        ),
    ]
