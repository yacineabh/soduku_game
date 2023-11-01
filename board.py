from const import *
from square import Sqaure
import random
import pygame


class Board():
    def __init__(self):
        self.squares=[[0,0,0,0,0,0,0,0,0] for row in range(rows)]
        self.random_array=[]
        self.game_values=[]
        self.paint=False
        for x in range(cols*rows):
            a=random.randint(0,1)
            b=random.randint(1,9) if a==1 else None
            self.random_array.append(b)
            
        self.create()
        self.add_values()
        
        
    def check_validity(self,row,col,value):
        
        #check line
        for i in range(cols):
            if self.squares[row][i].value==value and i!=col:
                return False
        
        for i in range(rows):
            if self.squares[i][col].value==value and i!=row:
                return False
        
        sqrow=row//3
        sqcol=col//3
        
        for i in range(sqrow+3):
            for j in range(sqcol+3):
                if i!=row and col!=col:
                    if self.squares[i][j]==value:
                        return False
        return True
    
    def colorize(self,screen,row,col):
        if not( (row,col) in self.game_values):
            self.paint=True
            color=(100, 204, 197)    
            rect=(col*sqsize,row*sqsize,sqsize,sqsize)
            pygame.draw.rect(screen,color,rect)
            
    def set_value(self,row,col,key):
        if key[pygame.K_0]:
            self.squares[row][col].value=0
        elif key[pygame.K_1]:
            self.squares[row][col].value=1
        elif key[pygame.K_2]:
            self.squares[row][col].value=2
        elif key[pygame.K_3]:
            self.squares[row][col].value=3
        elif key[pygame.K_4]:
            self.squares[row][col].value=4
        elif key[pygame.K_5]:
            self.squares[row][col].value=5
        elif key[pygame.K_6]:
            self.squares[row][col].value=6
        elif key[pygame.K_7]:
            self.squares[row][col].value=7
        elif key[pygame.K_8]:
            self.squares[row][col].value=8
        elif key[pygame.K_9]:
            self.squares[row][col].value=9
       
            
        
            
            
        
    def create(self):
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col]=Sqaure(row,col)
    
    def add_values(self):
        x=0
        for row in range(rows):
            for col in range(cols):
                value=self.random_array[x]
                if self.check_validity(row,col,value):
                    self.squares[row][col]=Sqaure(row,col,value)
                    self.game_values.append((row,col))
                x+=1
                
        
        
    
    