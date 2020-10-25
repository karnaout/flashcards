from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Deck(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    desc = models.CharField(max_length=255, null=False, blank=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"Title: {self.title} \nDescription: {self.desc}"

    # Returns total number of cards
    def total_cards(self):
        return self.card_set.count()

    # Returns total active number of cards
    def total_active_cards(self):
        return self.card_set.filter(is_active=True).count()    

class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"Question: {self.question} \nAnswer: {self.answer}"
