# Generated by Django 3.2.6 on 2021-12-02 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='unique_attribute',
            new_name='guid',
        ),
        migrations.RenameField(
            model_name='episode',
            old_name='publication_date',
            new_name='pub_date',
        ),
    ]
