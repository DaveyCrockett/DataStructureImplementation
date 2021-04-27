from Months import Months
from BirthdayPlaces import BirthdayPlaces
from SweepStakes import SweepStakes
from Node import Node
from linkedlist import LinkedList

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)
    linked_list.append_node_to_beginning(20)
    linked_list.append_data_after(linked_list.head.next, 30)
    print('The created linked list is: ')
    linked_list.print_nodes()
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
    trunk.pre_order(trunk)
