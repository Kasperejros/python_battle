import random

class Player:

    def __init__(self, name, hp, attack, defence):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
    

    def attack_enemy(self, opponent):
        damage = int((random.random() * self.attack) - (random.random() * opponent.defence))

        if int(damage) < 0:
            damage = 0

        print("{} done {} damage to {}".format(self.name, damage, opponent.name))
        return damage

    def take_damage(self, damage):
        self.hp -= damage
        print("{} has {} hp left".format(self.name, self.hp))