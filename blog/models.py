from django.db import models

class post_list(models.Model):
    url = models.CharField(max_length=255)
