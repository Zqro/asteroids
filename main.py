import pygame  # noqa: I001, RUF100
import sys

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player_sprite = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    astr_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # calculate dt (time since last frame, d = delta)
        dt = clock.tick(60) / 1000

        # draw sprite // not necessary???
        player_sprite.draw(screen)

        # updates game state using calculated dt
        updatable.update(dt)

        for item in asteroids:
            if item.collides_with(player_sprite):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for item in asteroids:
            for bullet in shots:
                if item.collides_with(bullet):
                    log_event("asteroid_shot")
                    item.split()
                    bullet.kill()

        # clears screen
        screen.fill("black")

        # draws everything at new position
        for item in drawable:
            item.draw(screen)

        # flips screen to show new frame
        pygame.display.flip()

if __name__ == "__main__":
    main()
