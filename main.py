from Months import Months
from BirthdayPlaces import BirthdayPlaces
from SweepStakes import SweepStakes
from Node import Node

if __name__ == '__main__':

    Months().pi_day()
    BirthdayPlaces().display_places()
    SweepStakes().pick_winner()
    trunk = Node(50)
    trunk = trunk.insert(trunk, 30)
    trunk = trunk.insert(trunk, 20)
    trunk = trunk.insert(trunk, 40)
    trunk = trunk.insert(trunk, 70)
    trunk = trunk.insert(trunk, 60)
    trunk = trunk.insert(trunk, 80)
    trunk.inorder(trunk)