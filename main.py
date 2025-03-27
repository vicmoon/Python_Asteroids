import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from  asteroidfield  import AsteroidField 

pygame.init()
font = pygame.font.Font(None, 74)  # 74 = font size

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")


background = pygame.image.load("background.jpg").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))




def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # ⚠️ Set containers on the class BEFORE creating the instancew 
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Game logic
        # update game logic 
        updatable.update(dt)
        #check collisions 

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                text = font.render("Game Over!", True, "white")
                text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

                screen.blit(text, text_rect)
                pygame.display.flip()  # Update the screen to show the text
                pygame.time.wait(2000)  # Pause 2 seconds so player can see it
                return


            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.splitting()
                    shot.kill() 

             
        # Drawing
        screen.blit(background, (0,0))
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        # Update dt
        dt = clock.tick(60) / 1000  

    pygame.quit()


if __name__ == "__main__":
    main()
