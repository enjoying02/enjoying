from django.db import models

class Friends(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()

    def __str__(self):
        return f'[{self.pk}]{self.title}'