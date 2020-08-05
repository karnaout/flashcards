from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Deck(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    desc = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"Title: {self.title} \nDescription: {self.desc}"

class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"Question: {self.question} \nAnswer: {self.answer}"
