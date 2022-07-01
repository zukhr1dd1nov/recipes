from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import get_language


class Kategoriya(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(default="23652806.jpg",blank=True,null=True)
    def __str__(self):
        return self.name

class Taom(models.Model):
    kategoriya = models.ForeignKey(Kategoriya,on_delete=models.RESTRICT)
    creator = models.ForeignKey(User,on_delete=models.RESTRICT)
    name = models.CharField(max_length=30)
    photo = models.ImageField(default="23652806.jpg",blank=True,null=True)
    text = models.TextField(null=True)
    comment_text = models.CharField(max_length=275)
    added_at = models.DateField(auto_now_add=True)
    portions = models.SmallIntegerField()
    how_much_time = models.DecimalField(max_digits=3,decimal_places=1)
    viewed = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name
