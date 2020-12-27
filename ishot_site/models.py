from django.db import models
from django import forms

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'CustomUser'


class Practice(models.Model):
    practice_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    place_url = models.URLField()
    date = models.DateField()
    start_time = models.TimeField()
    finish_time = models.TimeField()

    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Inquiry(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    title = models.CharField(max_length=30)
    message = models.TextField(max_length=100000)


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('1', '男性'),
        ('2', '女性'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, default=None)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=2, choices=GENDER_CHOICES)
    old = models.IntegerField()
    university = models.CharField(max_length=100, blank=True)
    grade = models.IntegerField(blank=True)
    experience = models.IntegerField()

    class Metal:
        verbose_name_plural = 'UserProfile'
