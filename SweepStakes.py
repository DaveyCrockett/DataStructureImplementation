import random


class SweepStakes:
    contestants = {
        'name': ['David Paredes', 'Tori Paredes', 'Carlos Paredes', 'Tina Paredes', 'Kim Paredes']
    }

    def pick_winner(self):
        choices = self.contestants.get('name')
        winner = random.choice(choices)
        print(winner)

