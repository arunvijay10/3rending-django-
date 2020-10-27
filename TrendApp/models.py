from django.db import models


# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=4000, default='')
    description = models.TextField()

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=4000, default='')
    description = models.TextField()
    images = models.ImageField(upload_to="uploads/images")
    date = models.DateTimeField()

    # we have to create a foriegn key with a cascade and link it with
    # the cateogry . when ever a image is deleted everything  gets deleted and on_delete is also used
    # we are passing class Cateogries in the foriegn key look down after the brackets

    cat = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __Str__(self):
        return self.title
