# Generated by Django 4.0 on 2024-07-19 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creatures', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creature',
            old_name='Ability',
            new_name='ability',
        ),
        migrations.RenameField(
            model_name='creature',
            old_name='Defense',
            new_name='defense',
        ),
        migrations.RenameField(
            model_name='creature',
            old_name='Power',
            new_name='power',
        ),
    ]