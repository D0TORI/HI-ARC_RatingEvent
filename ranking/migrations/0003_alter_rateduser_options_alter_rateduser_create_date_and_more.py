# Generated by Django 4.2.3 on 2023-09-14 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0002_remove_rateduser_userid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rateduser',
            options={'verbose_name': '유저', 'verbose_name_plural': '유저'},
        ),
        migrations.AlterField(
            model_name='rateduser',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='계정 생성시간'),
        ),
        migrations.AlterField(
            model_name='rateduser',
            name='userdiv',
            field=models.IntegerField(verbose_name='디비전'),
        ),
        migrations.AlterField(
            model_name='rateduser',
            name='username',
            field=models.CharField(max_length=200, verbose_name='핸들'),
        ),
        migrations.AlterModelTable(
            name='rateduser',
            table='RatedUser',
        ),
    ]