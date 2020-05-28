from django.db import models

# Create your models here.

class Todo(models.Model):
    added_date=models.DateTimeField('Date Added')
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Done(models.Model):
    done_date=models.DateTimeField('Date Added')
    done_text = models.CharField(max_length=200)

    def __str__(self):
        return self.done_text

