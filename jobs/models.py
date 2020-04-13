from django.db import models

class job(models.Model):
    # image = models.imageField(upload_t0='')
    field = models.ImageField(max_length=256,upload_to=''),
    summary = models.CharField(max_length=200)
    # this is new line