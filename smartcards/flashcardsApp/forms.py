from django.forms import ModelForm
from .models import Deck, Card

class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = ['title', 'desc', 'is_active']
        
class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['deck', 'is_active', 'question', 'answer']