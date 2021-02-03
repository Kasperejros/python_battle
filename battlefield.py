from player import *

class Battlefield:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.isBattle = True

    def update(self):
        self.player1.take_damage(self.player2.attack_enemy(self.player1))
        self.player2.take_damage(self.player1.attack_enemy(self.player2))

        if self.player1.hp <= 0 or self.player2.hp <= 0:
            self.isBattle = False