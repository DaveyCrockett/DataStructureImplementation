import random


class SweepStakes:

    def pick_winner(self):
        pick_one = random.choice(Contestants().contestantList)
        print(pick_one)


class Contestants:

    contestantList = [
        {
             'first_name': 'David',
             'last_name': 'Paredes'
        },
        {
            'first_name': 'Tori',
            'last_name': 'Paredes'
        },
        {
            'first_name': 'Tina',
            'last_name': 'Paredes'
        },
        {
            'first_name': 'Kim',
            'last_name': 'Paredes'
        },
        {
            'first_name': 'Carlos',
            'last_name': 'Paredes'
        }
    ]
