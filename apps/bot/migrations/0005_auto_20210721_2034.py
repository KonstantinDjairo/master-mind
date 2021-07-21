# Generated by Django 3.2.4 on 2021-07-21 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_auto_20210721_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donelist',
            name='edition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.edition'),
        ),
        migrations.AlterField(
            model_name='donelist',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.profile'),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.profile'),
        ),
        migrations.AlterField(
            model_name='taskbox',
            name='edition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.edition'),
        ),
        migrations.AlterField(
            model_name='taskbox',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.profile'),
        ),
    ]
