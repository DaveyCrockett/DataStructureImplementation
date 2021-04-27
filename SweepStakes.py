import random


class SweepStakes:

    def pick_winner(self):
        pick_one = random.choice(list(Contestants().contestantList.values()))
        print(pick_one)


class Contestants:

    contestantList = {
        'contestant_one': {
             'first_name': 'David',
             'last_name': 'Paredes'
         },
        'contestant_two': {
            'first_name': 'Tori',
            'last_name': 'Paredes'
        },
        'contestant_three': {
            'first_name': 'Tina',
            'last_name': 'Paredes'
        },
        'contestant_four': {
            'first_name': 'Kim',
            'last_name': 'Paredes'
        },
        'contestant_five': {
            'first_name': 'Carlos',
            'last_name': 'Paredes'
        }
    }
