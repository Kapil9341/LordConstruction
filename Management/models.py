from django.db import models


# Create your models here.
class QueryDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, default='')
    email = models.EmailField(max_length=50, blank=True, default='')
    subject = models.CharField(max_length=100, blank=True, default='')
    message = models.CharField(max_length=500, blank=True, default='')
    querydatetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class GetInTouch(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, default='')
    email = models.EmailField(max_length=50, blank=True, default='')
    phone = models.CharField(max_length=100, blank=True, default='')
    message = models.CharField(max_length=500, blank=True, default='')
    current_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
