from django.db import models

class Subject(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    price = models.IntegerField(default=0)
    #author:추후 작성예정

    def __str__(self):
        return f'[{self.pk}]{self.title}'
