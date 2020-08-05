from django.contrib import admin

from .models import *

def activate(modeladmin, request, queryset):
    queryset.update(is_active=True)

def deactivate(modeladmin, request, queryset):
    queryset.update(is_active=False)

class DeckAdmin(admin.ModelAdmin):
    list_display=('title', 'is_active', 'total_cards', 'total_active_cards')
    list_filter=('is_active',)
    actions = [activate,deactivate]

class CardAdmin(admin.ModelAdmin):
    list_display=('question', 'is_active')
    list_filter=('is_active',)
    actions = [activate,deactivate]
    
admin.site.register(Card, CardAdmin)
admin.site.register(Deck, DeckAdmin)    