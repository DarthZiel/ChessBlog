from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)
    url_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
