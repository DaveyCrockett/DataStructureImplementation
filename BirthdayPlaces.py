class BirthdayPlaces:
    def __init__(self):
        self.locations = {'Chuckee Cheese', 'Home', 'McDonalds', 'Round Table', 'Medieval Times'}
        self.future_locations = {'Dave n Busters', 'Taco Bell', 'Big Bear'}

    def push_location(self):
        setunion = self.locations.union(self.future_locations)
        return setunion

    def display_places(self):
        for i in self.push_location():
            print(i)
