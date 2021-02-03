import random

class Player:

    def __init__(self, name, hp, attack, defence):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
    

    def attackEnemy(self, opponent):
        damage = int((random.random() * self.attack) - (random.random() * opponent.defence))

        if int(damage) < 0:
            damage = 0

        print("{} done {} damage to {}".format(self.name, damage, opponent.name))
        return damage

    def takeDamage(self, damage):
        self.hp -= damage
        print("{} has {} hp left".format(self.name, self.hp))

    def isAlive(self):
       return True if self.hp > 0 else False
