from django.db import models


class predict_model(models.Model):
    # 모델 이름
    model_name = models.CharField(max_length=50)
    # 저장 위치
    model_path = models.CharField(max_length=50)

    # 학습 데이터 범위
    train_datetime = models.DateTimeField()
    train_interval = models.IntegerField()
    # 예측 데이터 범위
    predict_interval = models.IntegerField()

    # 예측 주기
    train_cycle = models.IntegerField()
    # 예측 주기
    predict_cycle = models.IntegerField()


class generation_atv_power(models.Model):
    # 장비 정보
    site_id = models.CharField(max_length=50)
    perf_id = models.SmallIntegerField()

    # 목표 날짜
    target = models.DateTimeField()
    # 발행 날짜
    issued = models.DateTimeField(auto_now_add=True)  # 예측 수행 날짜
    # 예측 데이터
    predict = models.FloatField()
    # 오차
    error = models.FloatField()

