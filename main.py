from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
import pygame
from logger import log_state
import os
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys
from circleshape import *
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}", "Screen width: 1280", "Screen height: 720")
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)


    os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
    pygame.init()
    AsteroidField()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        updatable.update(dt)
        
        for obj in asteroids:
            for shot in shots:
                if obj.collides_with(shot) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    obj.split()

        
        
        for obj in asteroids:
            if player.collides_with(obj) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        screen.fill(pygame.Color("black"))
        for obj in drawable:
            obj.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
