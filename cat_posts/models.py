from django.db import models
from django.contrib.auth import get_user_model

class Cats(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=26)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    admin = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        return self.name