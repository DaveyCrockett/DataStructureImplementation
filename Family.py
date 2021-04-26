class Family:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.relationship = ''

        member_one = Family()
        member_one.first_name = 'Tori'
        member_one.last_name = 'Paredes'
        member_one.relationship = 'Wife'

        member_two = Family()
        member_two.first_name = 'Cole'
        member_two.last_name = 'Paredes'
        member_two.relationship = 'Son'

        member_three = Family()
        member_three.first_name = 'Liam'
        member_three.last_name = 'Paredes'
        member_three.relationship = 'Son'

        member_four = Family()
        member_four.first_name = 'Cayden'
        member_four.last_name = 'Paredes'
        member_four.relationship = 'Son'

        self.members = [member_one, member_two, member_three, member_four]