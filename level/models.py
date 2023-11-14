from django.db import models

class Subject(models.Model):
    head_image = models.ImageField(upload_to='level/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='level/files/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=40)
    content = models.TextField()
    price = models.IntegerField(default=0)
    #author:추후 작성예정


    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/level/{self.pk}/'
