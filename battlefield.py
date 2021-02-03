from player import *

class Battlefield:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def update(self):
        self.player1.takeDamage(self.player2.getAttackDamage())
        self.player2.takeDamage(self.player1.getAttackDamage())



    def isFinished(self):
        return False if self.player1.isAlive() and self.player2.isAlive() else True