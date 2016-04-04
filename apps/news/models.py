from django.db import models


class New(models.Model):
    content = models.CharField(max_length=200)
    first_img = models.ImageField()
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=200)

    #L'image la plus récente sera mise à la une
