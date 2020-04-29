from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class JWTPayloadTrack(models.Model):
    username = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    iat = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'JWT Payload Tracks'

    def __str__(self):
        return self.username
