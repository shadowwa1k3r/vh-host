from django.db import models


class Video(models.Model):
    progress = models.TextField(null=True, blank=True)
    result = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'video'
    
    def __str__(self):
        return self.name