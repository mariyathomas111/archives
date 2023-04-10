from django.db import models

class Record(models.Model):
  id = models.TextField(max_length=355,primary_key=True, unique=True)
  title = models.CharField(max_length=255,blank=True, null=True)
  desc = models.CharField(max_length=255,blank=True, null=True)
  citablereference=models.CharField(max_length=255,blank=True, null=True)