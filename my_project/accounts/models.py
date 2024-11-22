from django.db import models
from django.contrib.auth.models import User

class ImageList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    response_codes = models.JSONField()  # A list of response codes
    image_links = models.JSONField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
