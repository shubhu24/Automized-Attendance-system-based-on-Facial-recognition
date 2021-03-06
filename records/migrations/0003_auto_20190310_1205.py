# Generated by Django 2.1.2 on 2019-03-10 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20190310_0139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='records',
            old_name='country',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='records',
            old_name='marital_status',
            new_name='roll_no',
        ),
        migrations.RenameField(
            model_name='records',
            old_name='residence',
            new_name='section',
        ),
        migrations.RemoveField(
            model_name='records',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='records',
            name='education',
        ),
        migrations.RemoveField(
            model_name='records',
            name='occupation',
        ),
        migrations.AddField(
            model_name='records',
            name='active',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
