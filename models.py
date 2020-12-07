from django.db import models
class Contact(models.Model):
    name=models.CharField(max_length=40)
    mobile=models.CharField(max_length=10)
    email=models.CharField(max_length=40)
    feedback=models.TextField(max_length=200)

    def __str__(self):
        return self.name


def details():
    return None