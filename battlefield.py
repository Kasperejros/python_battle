from player import *

class Battlefield:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def update(self):
        self.player1.takeDamage(self.player2.attackEnemy(self.player1))
        self.player2.takeDamage(self.player1.attackEnemy(self.player2))



    def isFinished(self):
        if self.player1.isAlive() and self.player2.isAlive():
            return False
        else:
            return True