from django.db import models

# Create your models here.
# from models import Comments



class Posts(models.Model):
    post = models.CharField(max_length=200)
    comment = models.ManyToManyField('Comments')

    class Meta:
        ordering = ('post',)


class Comments(models.Model):
    post = models.ForeignKey(Posts)
    comment = models.CharField(max_length=200)

    class Meta:
        ordering = ('comment',)