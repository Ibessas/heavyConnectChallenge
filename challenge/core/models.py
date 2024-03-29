from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Report(models.Model):
    message = models.CharField(max_length=50)
    author = models.ForeignKey(
        User,related_name="custom_user_profile",
        on_delete=models.CASCADE,
    )
    supervisor = models.ManyToManyField(
        User)

admin.site.register(Report)

class ReportResponse(models.Model):
    message = models.CharField(max_length=50)
    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )
admin.site.register(ReportResponse)
