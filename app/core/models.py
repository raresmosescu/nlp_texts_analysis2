from django.db import models

# Create your models here.
class Noun(models.Model):
	result_id = models.IntegerField()
	word = models.CharField(max_length=30)
	freq = models.IntegerField()
	score = models.FloatField()
