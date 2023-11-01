from const import *
import sys
import pygame
from board import Board

pygame.init()
class Game():
    def __init__(self) :
        self.board=Board()
    
    def show_bg(self,screen):
        screen.fill((255,255,255))
        for col in range(cols):
            line_width=7 if col%3==0 else 2
            pygame.draw.line(screen,(0,0,0),(col*sqsize,0),(col*sqsize,height_screen),line_width)
            pygame.draw.line(screen,(0,0,0),(0,col*sqsize),(width_screen,col*sqsize),line_width)
        
        
    def show_numbers(self,screen):
        font=pygame.font.SysFont("None",50)
        
        for row in range(rows):
            for col in range(cols):
                if self.board.squares[row][col].has_value():
                    value=self.board.squares[row][col].value
                    
                    if not((row,col) in self.board.game_values):
                        if self.board.check_validity(row,col,value):
                            color=(0,0,0)
                        else:
                            color=(255,0,0)
                    else :
                        color=(0,0,0)
                    rendered=font.render(str(value),0,color)
                    rendered_rect=rendered.get_rect(center=(sqsize*col+sqsize//2,sqsize*row+sqsize//2))
                    screen.blit(rendered,rendered_rect)                    
        
    
            
            