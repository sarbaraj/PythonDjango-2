from django.db import models

# Create your models here.

class BannerText(models.Model):
    id = models.IntegerField(primary_key=True)
    banner_text = models.CharField(max_length=250)

    def __str__(self):
        return str(self.id)+", "+self.banner_text