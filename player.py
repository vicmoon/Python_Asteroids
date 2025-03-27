from circleshape import CircleShape
from constants import *
from shot import Shot
import pygame 

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0


    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2) 

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer = max(0, self.timer - dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)  #turn Left
        if keys[pygame.K_d]:
            self.rotate(dt)   #turn Right 
        if keys[pygame.K_w]:
            self.move(dt)  
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

        
    def shoot(self):
        if self.timer > 0:
            return  #still in cooldown

        #shoot fire

        direction = pygame.Vector2(0,1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = direction * PLAYER_SHOOT_SPEED

        #reset cooldown timer

        self.timer = PLAYER_SHOOT_COOLDOWN
       
        




        
