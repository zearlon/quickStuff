from candy import Candy


class Person:
    def __init__(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position


class Kid(Person):
    def __init__(self, position, initiative):
        super().__init__(position)
        self.initiative = initiative
        self.candy_list = []
        self.obtained_uranium = 0
        self.visited_hosts = []

    def get_initiative(self):
        return self.initiative

    def add_candy(self, candy):
        self.candy_list.append(candy)
        self.obtained_uranium += candy.get_uranium_quantity()

    def is_critical(self):
        if self.obtained_uranium > 20:
            return True
        return False

    def host_visited(self, host):
        self.visited_hosts.append(host)

    def find_closest_host(self, participants_list):
        distance = 0
        closest_host = 0

        for participant in participants_list:
            if participant in self.visited_hosts:
                continue

            if type(participant).__name__ == "Host":
                distanceX = abs(participant.get_position()[0] - self.get_position()[0])
                distanceY = abs(participant.get_position()[1] - self.get_position()[1])

                if distance == 0 or (distanceX + distanceY < distance and distanceX+distanceY > 0):
                    distance = distanceX + distanceY
                    closest_host = participant

        return closest_host




class Host(Person):
    def __init__(self, position, candies):
        super().__init__(position)
        self.candies = candies
        self.basket = self.fill_basket()

    def fill_basket(self):
        basket = []

        for candy in self.candies:
            basket.append(Candy(*candy))
        return basket


    def remove_candy(self, candy_function):
        if not self.candies:
            return None

        return candy_function(self.basket)



