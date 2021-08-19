from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=150)

    def __str__(self):
        return (f'Email: {self.email} ---------> Subject: {self.subject} ----------> Message:{self.message}')
