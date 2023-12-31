# Generated by Django 4.2.3 on 2023-09-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0004_alter_rateduser_options_rateduser_userrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rateduser',
            name='seasonStartRating',
            field=models.IntegerField(default=0, verbose_name='시즌 시작 레이팅'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rateduser',
            name='userrating',
            field=models.IntegerField(verbose_name='현재 레이팅'),
        ),
    ]
