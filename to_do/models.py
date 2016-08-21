import datetime

from django.db import models


class Task(models.Model):

    completed = models.BooleanField(default=False)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    modified_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.now()
        self.modified_at = datetime.datetime.now()

        super(Task, self).save(*args, **kwargs)