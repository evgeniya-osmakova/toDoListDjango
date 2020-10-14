import uuid
from django.db import models
import datetime

class Task(models.Model):
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4, editable=False)
    task = models.CharField('task', max_length=50)
    # date = models.DateField('date', default=datetime.date.today, auto_now=False, auto_now_add=False)
    done = models.BooleanField('done', default=False)
