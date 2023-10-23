import random
import json


class Cards:
    def __init__(self):
        with open('settings.json', 'r', encoding='utf-8') as fh:
            self.settings = json.load(fh)
            fh.close()
        self.special_cards = ['Pickup 2', 'Skip', 'Reverse']
        self.cards = []
        self.played_cards = []
        self.player_cards = []

    def change_setting(self, setting, new):
        self.settings[setting] = new
        with open('settings.json', 'w', encoding='utf-8') as fh:
            json.dump(self.settings, fh)
            fh.close()

    def generate_cards(self):
        for _ in range(2):
            for color in range(len(self.settings['Colors'])):
                self.cards.append([f'{self.settings['Colors'][color]} {i}'
                                  for i in range(10)])
                self.cards.append([f'{self.settings['Colors'][color]} {i}'
                                  for i in self.special_cards])
        for _ in range(4):
            self.cards.append(['Wild', 'Wild Pickup 4'])
        self.cards = sum(self.cards, [])
        for color in self.settings['Colors']:
            self.cards.remove(f'{color} 0')

    def deal_card(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card

    def deal_cards(self):
        for _ in range(self.settings['PlayerCount']):
            templist = []
            for _ in range(7):
                templist.append(self.deal_card())
            self.player_cards.append(templist)
