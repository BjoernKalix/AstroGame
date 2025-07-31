import pygame
from circleshape import CircleShape
from constants import *
SHOT_RADIUS = 5
class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position, velocity, SHOT_RADIUS)
        self.velocity = velocity
        
    

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),self.position,SHOT_RADIUS,2)

    def update(self, dt):
        self.position += (self.velocity * dt)