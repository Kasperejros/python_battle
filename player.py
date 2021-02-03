import random

class Player:

    def __init__(self, name, hp, attack, defence):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
    

    def getAttackDamage(self):
        damage = int(random.random() * self.attack)
        return damage if damage > 0 else 0

    def takeDamage(self, damageDone):
        damageTaken = int(damageDone - (random.random() * self.defence))
    
        if damageTaken > 0:
            self.hp -= damageTaken
            print("{} has taken {} damage".format(self.name, damageTaken))
        else:
            print("{} has taken 0 damage".format(self.name))
        if self.hp > 0:
            print("{} has {} hp left".format(self.name, self.hp))
        else:
            print("{} has died".format(self.name))

    def isAlive(self):
       return self.hp > 0
