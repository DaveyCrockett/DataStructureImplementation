class BirthdayPlaces:
    def __init__(self):
        self.locations = ['Chuckee Cheese', 'Home', 'McDonalds', 'Round Table', 'Medieval Times']
        self.future_locations = ['Dave n Busters', 'Taco Bell', 'Big Bear']

    def push_location(self):
        self.locations.extend(self.future_locations)

    def display_places(self):
        self.push_location()
        for i in self.locations:
            print(i)
