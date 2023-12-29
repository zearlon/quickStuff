class Candy:
    def __init__(self, mass, uranium):
        self.mass = mass
        self.uranium = uranium

    def get_uranium_quantity(self):
        return self.mass*self.uranium

    def get_mass(self):
        return self.mass
