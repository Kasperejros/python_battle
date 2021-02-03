from player import *
from battlefield import *

player1 = Player("Kacper", 100, 50, 40)
player2 = Player("Arek", 100, 50, 40)

battlefield = Battlefield(player1, player2)

#gameloop
while not battlefield.isFinished():
    battlefield.update()