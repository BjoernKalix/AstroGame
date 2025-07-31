import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)


    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),self.position,self.radius,2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif self.radius > ASTEROID_MIN_RADIUS and self.radius <= ASTEROID_MAX_RADIUS:
            radius_neu = random.uniform(20,50)
            self.radius -= ASTEROID_MIN_RADIUS        
            asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid_1.velocity = pygame.math.Vector2.rotate(self.velocity, radius_neu)*1.2
            asteroid_2.velocity = pygame.math.Vector2.rotate(self.velocity, -radius_neu)*1.2
        else:
            radius_neu = random.uniform(20,50)
            self.radius -= ASTEROID_MAX_RADIUS        
            asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid_1.velocity = pygame.math.Vector2.rotate(self.velocity, radius_neu)*1.2
            asteroid_2.velocity = pygame.math.Vector2.rotate(self.velocity, -radius_neu)*1.2
            







