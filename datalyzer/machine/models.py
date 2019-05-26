from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Data(models.Model):
    data_json = models.TextField()
    features_json = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300, blank=True)
    is_public = models.BooleanField(default=False)
    create_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
