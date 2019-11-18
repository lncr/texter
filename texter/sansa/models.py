from django.db import models
from time import time


class InputText(models.Model):
	body = models.TextField()