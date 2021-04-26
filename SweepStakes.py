import random


class SweepStakes:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''

    def pick_winner(self):
        pick_one = random.choice(Contestants().contestant_list)
        print(pick_one.first_name + ' ' + pick_one.last_name)


class Contestants:
    def __init__(self):
        super().__init__()

        contestant_one = SweepStakes()
        contestant_one.first_name = 'David'
        contestant_one.last_name = 'Paredes'

        contestant_two = SweepStakes()
        contestant_two.first_name = 'Tori'
        contestant_two.last_name = 'Paredes'

        contestant_three = SweepStakes()
        contestant_three.first_name = 'Tina'
        contestant_three.last_name = 'Paredes'

        contestant_four = SweepStakes()
        contestant_four.first_name = 'Carlos'
        contestant_four.last_name = 'Paredes'

        contestant_five = SweepStakes()
        contestant_five.first_name = 'Kim'
        contestant_five.last_name = 'Paredes'

        self.contestant_list = [contestant_one, contestant_two, contestant_three, contestant_four, contestant_five]