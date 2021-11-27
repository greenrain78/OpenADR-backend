from django.contrib.postgres.fields.array import ArrayField
from django.db import models


# Create your models here.
class container(models.Model):
    name = models.CharField(max_length=50, unique=True)

    image_name = models.CharField(max_length=50)
    image_version = models.CharField(max_length=50, null=True)

    engine = ArrayField(
        models.CharField(max_length=50, blank=True), null=True
    )
    # 위는 직접 작성, 아래는 자동 입력
    container_id = models.CharField(max_length=100, null=True)
    environment = ArrayField(
        models.CharField(max_length=50, blank=True), null=True
    )

    network = models.CharField(max_length=50, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    command = models.CharField(max_length=50, null=True)  # 명령어를 입력하여 사용
    status = models.CharField(max_length=50, null=True)  # docker 에서 정의한 상태
    state = models.CharField(max_length=50, null=True)  # 내가 정의한 상태

    dockerfile = models.CharField(max_length=50, null=True)


class engine(models.Model):
    name = models.CharField(max_length=50)  # 객체 이름
    module_name = models.CharField(max_length=50)  # 파일 이름
    container_name = models.CharField(max_length=50)  # 들어있는 컨테이너 이름

    cycle = ArrayField(  # 스케줄러 주기
        ArrayField(
            models.CharField(max_length=10, blank=True),
            null=True,
        )
    )
    # db 연결을 위한 네트워크 연결
    network = models.CharField(max_length=50, null=True)

    # 생성된 시각
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    # 상태 정보
    status = models.CharField(max_length=50, null=True)


class logs(models.Model):
    # 프로세스 정보
    container = models.CharField(max_length=50)
    process = models.IntegerField()
    process_name = models.CharField(max_length=50)
    thread = models.BigIntegerField()
    thread_name = models.CharField(max_length=50)

    # 위치 정보
    name = models.CharField(max_length=50)
    pathname = models.CharField(max_length=200)
    func_name = models.CharField(max_length=50)
    lineno = models.IntegerField()

    levelno = models.IntegerField()
    levelname = models.CharField(max_length=50)
    time = models.DateTimeField()

    # 메세지
    message = models.TextField(blank=True)
    exc_info = models.TextField(blank=True)
    exc_text = models.TextField(blank=True)
    stack_info = models.TextField(blank=True)
