# Generated by Django 3.2.6 on 2021-12-04 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0002_auto_20211202_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='pub_date',
            new_name='publication_date',
        ),
        migrations.RenameField(
            model_name='episode',
            old_name='guid',
            new_name='unique_attribute',
        ),
    ]
