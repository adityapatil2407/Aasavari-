from django.db import models

# Create your models here.
# models.py



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    sent_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.timestamp}"


