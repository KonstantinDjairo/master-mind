# Generated by Django 3.2.4 on 2021-07-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_auto_20210721_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leveluser',
            old_name='check',
            new_name='prestige',
        ),
        migrations.AddField(
            model_name='leveluser',
            name='prestige_level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
