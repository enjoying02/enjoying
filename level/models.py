from django.db import models
from django.contrib.auth.models import User
import os

class Subject(models.Model):
    head_image = models.ImageField(upload_to='level/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='level/files/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=40)
    content = models.TextField()
    price = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/level/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

