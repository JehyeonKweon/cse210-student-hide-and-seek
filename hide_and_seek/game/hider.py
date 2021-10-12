import random

# TODO: Define the Hider class here

class Hider:

    def __init__(self):
        
        self.location = random.randint(1, 1000)
        self.distance = [1000, 1000]

    def watch(self, location):

        distance = abs(self.location - location)
        self.distance.append(distance)

    def get_hint(self):

        if self.distance[-1] == 0:
            hint = '(;.;) You found me..'

        elif self.distance[-1] > self.distance[-2]:
            hint = '(^.^) Getting colder!'
        
        elif self.distance[-1] < self.distance[-2]:
            hint = '(>.<) Getting warmmer!'


        return hint