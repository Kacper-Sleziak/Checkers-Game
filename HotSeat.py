from Game import Game
from Player import Player
import pygame

class HotSeat():

    def __init__(self, width, height, window, redPlayer, bluePlayer, game):
        super().__init__()
        self.width = width
        self.height = height
        self.window = window
        self.redPlayer = redPlayer
        self.bluePlayer = bluePlayer
        self.game = game

    def hotSeatGame(self):
        turn = 0
        running = True
        while running:
            if turn % 2 == 0:
                running = self.game.singleRound(self.redPlayer, self.bluePlayer)[0]
            elif turn % 2 == 1:
                running = self.game.singleRound(self.bluePlayer, self.redPlayer)[0]

            turn += 1
