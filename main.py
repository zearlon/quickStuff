from collections import defaultdict
from person import *

def return_candy(candies):
    massive_candy = Candy(0, 0.0)
    for candy in candies:
        if candy.get_mass() > massive_candy.get_mass():
            massive_candy = candy

    return massive_candy

class FluxCapacitor:
    def __init__(self, participants):
        self.participants = participants
        self.isContinue = True

        while self.isContinue:
            if self.change_hosts() is None:
                return None
            death_result = self.give_candy()
            if death_result != 0:
                self.get_victim(death_result)

    def change_hosts(self):
        self.host_doors = defaultdict(list)
        for participant in self.participants:
            if type(participant).__name__ == "Kid":
                host = participant.find_closest_host(self.participants)

                #if there are no hosts left to visit
                if host == 0:
                    self.isContinue = True
                    return None
                
                participant.set_position(host.get_position())
                self.host_doors[host].append(participant)

        return 0

    def give_candy(self):
        for host in self.host_doors:
            #sort kids based on initiative
            self.host_doors[host].sort(key=lambda x: x.initiative, reverse=True)
            
            for kid in self.host_doors[host]:
                candy = host.remove_candy(return_candy)
                kid.add_candy(candy)

                if kid.is_critical():
                    self.isContinue = False
                    return self.host_doors[host]
        return 0

    def get_victim(self, death_result):
        for death in death_result:
            print(death.position)

if __name__ == '__main__':
    candy = Candy(20, 0.3)
    person = Person((1, 2))
    kid = Kid((0, 0), 123)
    host = Host((3, 4), [(1, 1.0), (2, 0.5)])
    flux_capacitor = FluxCapacitor({kid, host})
