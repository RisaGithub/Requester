from django.db import models


class URL(models.Model):
    url = models.CharField(max_length=1000)
    is_active = models.BooleanField()
    time_interval = models.TimeField()
    request_method = models.CharField(max_length=10)
    next_request_time = models.TimeField(auto_now_add=True)


class Request(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE)
    sent_at = models.DateTimeField()
    http_status_code = models.CharField(max_length=10)
    request_method = models.CharField(max_length=10)
    error_message = models.CharField(max_length=1000)
