from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SubmitAttendance(models.Model):

    class Meta:
        db_table = 'attendance'

    IN_OUT_STATUS = (
        (0, '退出'),
        (1, '入室'),
        (2, '外出'),
        (3, '休憩'),
        (4, 'リモート'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    in_out = models.IntegerField(verbose_name='IN/OUT', choices=IN_OUT_STATUS, default=None)
    time = models.TimeField(verbose_name="打刻時間")
    date = models.DateField(verbose_name='打刻日')
