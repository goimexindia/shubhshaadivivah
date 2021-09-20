from django.db import models


class Contactme(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=60)
    mobile = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    date_reg1 = models.DateTimeField(auto_now_add=True)

