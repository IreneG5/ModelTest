# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Contact(models.Model):

    class Meta:
        app_label = "ModelTest_app"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=25)

    def __str__(self):
        return ' '.join([
            self.first_name,
            self.last_name,
        ])
