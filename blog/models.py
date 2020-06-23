from django.db import models

from django.urls import reverse

# Create your models here.

class Post(models.Model):
    # post başlığı
    title = models.CharField(max_length=200)

    # yazar bilgileri
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)

    # post içeriği
    body = models.TextField()

    # admin panelinde görülecek post ismi
    def __str__(self):
        return self.title
    
    # templateler üzerinden contex(model context).pk üzerinden pk ya erişilir
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    
    


    