from django.db import models

# Create your models here.

class RatedUser(models.Model):
    username = models.CharField(max_length=200, unique=True, verbose_name='핸들')
    seasonStartRating = models.IntegerField(verbose_name='시즌 시작 레이팅')
    userrating = models.IntegerField(verbose_name='현재 레이팅')
    userdiv = models.IntegerField(verbose_name='디비전')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='계정 생성시간')

    class Meta:
        db_table = 'RatedUser'
        verbose_name = 'RatedUser'
        verbose_name_plural = 'RatedUser'