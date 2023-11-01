import pygame
from game import Game
from const import *

class Main():
    def __init__(self) :
        self.screen=pygame.display.set_mode((width_screen,height_screen))
        pygame.display.set_caption('soduku')
        self.game=Game()
        
    def mainloop(self):
        run=True
        game=self.game
        board=self.game.board
        screen=self.screen
        
        while run:
            game.show_bg(screen)
            game.show_numbers(screen)
            if board.paint:
                board.colorize(screen,clicked_row,clicked_col)
                
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    clicked_row=int(event.pos[1]//sqsize)
                    clicked_col=int(event.pos[0]//sqsize)
                    board.colorize(screen,clicked_row,clicked_col)
                    
                    
                elif event.type==pygame.KEYDOWN:
                    board.paint=False
                    key=pygame.key.get_pressed()
                    board.set_value(clicked_row,clicked_col,key)
                
                elif event.type==pygame.QUIT:
                    run=False
                
            
            pygame.display.update()
        
    
main=Main()
main.mainloop()