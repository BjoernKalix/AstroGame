import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
   

    Player.containers = (updatable,drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0,0,0))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit("Game over!")

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    pygame.sprite.Sprite.kill(shot)
        for draws in drawable:
            draws.draw(screen)




        
        
        
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
