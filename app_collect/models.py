from django.db import models


# Create your models here.
from django.db.models.deletion import CASCADE
from django.utils import timezone


class power_dashboard(models.Model):
    # power info 를 한눈에 보기 위해서 제작
    site_id = models.CharField(max_length=50)
    perf_id = models.SmallIntegerField()

    # 하루 단위로 작성
    ymdms = models.DateTimeField(default=timezone.now)

    # 데이터 길이
    data_length = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)


class equipments_info(models.Model):
    site_id = models.CharField(max_length=50)
    perf_id = models.SmallIntegerField()

    eqp_code = models.CharField(max_length=200)
    eqp_name = models.CharField(max_length=200)
    eqp_type = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)


class power_info(models.Model):
    site_id = models.CharField(max_length=50)
    perf_id = models.SmallIntegerField()
    dashboard_id = models.IntegerField()
    # dashboard_id = models.ForeignKey(power_dashboard, on_delete=CASCADE, related_name='dashboard2power_info')

    pn_name = models.CharField(max_length=50)
    eqp_name = models.CharField(max_length=50)
    ymdms = models.DateTimeField()

    vol_tage = models.FloatField()
    am_pere = models.FloatField()
    ar_power = models.FloatField()
    atv_power = models.FloatField()
    rat_power = models.FloatField()
    pw_factor = models.FloatField()
    accrue_power = models.FloatField()
    voltager_s = models.FloatField()
    voltages_t = models.FloatField()
    voltaget_r = models.FloatField()
    temperature = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
