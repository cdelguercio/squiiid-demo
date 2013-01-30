from django.db import models

class SquiiidImage(models.Model):
    image = models.FileField(upload_to='images')
    name = models.CharField(max_length=10000)
    photographer = models.CharField(max_length=10000)
    date = models.DateTimeField()

    def __unicode__(self):
        return unicode('')

class Tag(models.Model):
    image = models.ForeignKey(SquiiidImage)
    url = models.CharField(max_length=10000)
    x = models.IntegerField()
    y = models.IntegerField()
    date = models.DateTimeField()

    def __unicode__(self):
        return unicode('')