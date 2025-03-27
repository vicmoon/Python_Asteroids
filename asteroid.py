from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt 

    def splitting(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  #small asteroid 
        
        #Step 1 : generate random angle between(20, 50)

        random_angle = random.uniform(20, 50)

        #Step 2 : rotate velocity in opposite directions 
        direction1 = self.velocity.rotate(random_angle) * 1.2
        direction2 = self.velocity.rotate(-random_angle) * 1.2


        #Step3 : compute new radius 

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        #Step 4 : create two new asteroids 

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = direction1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = direction2



