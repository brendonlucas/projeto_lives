from django.db import models


# Create your models here.
class Fac(models.Model):
    nome = models.CharField(max_length=150)


class Canal(models.Model):
    nome = models.CharField(max_length=150)
    nick_player = models.CharField(max_length=150, null=True)
    link_yt = models.CharField(max_length=250, null=True, default='#')
    link_kick = models.CharField(max_length=250, null=True, default='#')
    link_tw = models.CharField(max_length=250, null=True, default='#')
    fac_player = models.ForeignKey(Fac, on_delete=models.CASCADE, null=True)
