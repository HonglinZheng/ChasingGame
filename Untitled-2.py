import pygame
import random
from abc import ABC, abstractmethod
#ABC means Abstract Base Class

pygame.init()

#color
RED = (255,0,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

# initiate the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Rectangle(ABC):
    @abstractmethod
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect((x,y,width,height))
        self.color = color
    
    def show(self):
        pygame.draw.rect(SCREEN, self.color, self.rect)

class Player(Rectangle):
    def __init__(self, x, y, width, height, color, step):
        super().__init__(x, y, width, height, color)
        self.step = step
    
    def accelerate(self):
        self.step+=0.5
        
    def moveTo(self, x, y):
        # Define the function to move object to position x, y
        if x > 0 and x < SCREEN_WIDTH and y > 0 and y < SCREEN_HEIGHT:
            self.rect.topleft = (x,y)

    def random_position(self):
        # Define the function to move object to a random position
        new_x = random.randint(50,750)
        new_y = random.randint(50,550)
        self.moveTo(new_x, new_y)
            
    # Define four functions to move object by 1 step in each direction
    def move_left(self):
        if self.rect.left - self.step >= 0:
            new_x = self.rect.x-self.step
            self.moveTo(new_x, self.rect.y)
    
    def move_down(self):
        if self.rect.bottom + self.step <= SCREEN_HEIGHT:
            new_y = self.rect.y+self.step
            self.moveTo(self.rect.x, new_y)

    def move_up(self):
        if self.rect.top - self.step >= 0:
            new_y = self.rect.y-self.step
            self.moveTo(self.rect.x, new_y)
        
    def move_right(self):
        if self.rect.right + self.step <= SCREEN_WIDTH:
            new_x = self.rect.x+self.step
            self.moveTo(new_x, self.rect.y)
    
    def collision(self, other):
        # Define the function to detect collision
        if (self.rect.left >= other.rect.left and self.rect.left <= other.rect.right) or (self.rect.right <= other.rect.right and self.rect.right >= other.rect.left):
            if (self.rect.top >= other.rect.top and self.rect.top <= other.rect.bottom) or (self.rect.bottom <= other.rect.bottom and self.rect.bottom >= other.rect.top):
                return True
        return False

class Text(Rectangle):
    def __init__(self, x, y, width, height, box_color, text, text_color):
        super().__init__(x, y, width, height, box_color)
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None,36)
        self.text = text
        self.text_color = text_color
    
    def show(self):
        super().show()
        text_surface = self.font.render(self.text, True, self.text_color)
        SCREEN.blit(text_surface, (self.x,self.y))
    
    def collidepoint(self,pos):
        return self.rect.collidepoint(pos)

# initiate objects
player_1 = Player(50,50,20,20,RED,1)
player_2 = Player(750,550,20,20,YELLOW,1)
play_again = Text(450,550,270,30,WHITE, "CLICK TO PLAY AGAIN",BLACK)
game_over = Text(320,280,150,30,BLACK,"GAME OVER",WHITE)

def main():
# main body
    run = True
    while run:
        SCREEN.fill(BLACK)
    
        player_1.show()
        player_2.show()
    
        if player_1.collision (player_2): # collision detected and freeze the screen
            game_over.show()
            play_again.show()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and play_again.collidepoint(event.pos):
                    player_1.random_position()
                    player_2.random_position()
                    player_1.accelerate()
                    player_2.accelerate()

        else:# in the active moving state
    
            key = pygame.key.get_pressed()
    
            if key[pygame.K_a]:
                player_1.move_left()
            if key[pygame.K_d]:
                player_1.move_right()
            if key[pygame.K_w]:
                player_1.move_up()
            if key[pygame.K_s]:
                player_1.move_down()
    
            if key[pygame.K_LEFT]:
                player_2.move_left()
            if key[pygame.K_RIGHT]:
                player_2.move_right()
            if key[pygame.K_UP]:
                player_2.move_up()
            if key[pygame.K_DOWN]:
                player_2.move_down()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        pygame.display.update()
    
 
    pygame.quit()

main()

'''
Object-Oriented Programming:
    An object is an instance of a class.
    Class is blueprint; object is an entity based on this blueprint
    Abstract class doens't have instances.

Four principles of OOP:
    Abstraction
    Inheritance
    Encapsulation
    Polymorphism
    
'''