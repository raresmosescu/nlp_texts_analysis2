from django.db import models

class Feedbacks(models.Model):
  feedback = models.TextField(max_length=10000)
