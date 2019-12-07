# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from  datetime import datetime

from django.db import models

class Todo(models.Model):
    STATUS_CHOICES = (
        ('PROCESS', 'Process'),
        ('COMPLETED', 'Completed'),
        ('PENDING','Pending'),
    )
    title= models.CharField(max_length=200)
    description=models.TextField()
    dateTime =models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='Process')


    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return self.title


