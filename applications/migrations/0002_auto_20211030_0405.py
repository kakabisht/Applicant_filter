# Generated by Django 3.1.3 on 2021-10-30 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='in_a_group_whichin_a_group_which_person_has_your_attention',
            new_name='in_a_group_which_person_has_your_attention',
        ),
    ]
