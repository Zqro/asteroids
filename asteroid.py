import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rotation = random.uniform(20, 50)
            astr1_vec = self.velocity.rotate(rotation)
            astr2_vec = self.velocity.rotate(-rotation)
            new_astr_rad = self.radius - ASTEROID_MIN_RADIUS

            astr1 = Asteroid(self.position.x, self.position.y, new_astr_rad)
            astr2 = Asteroid(self.position.x, self.position.y, new_astr_rad)

            astr1.velocity = astr1_vec * 1.2
            astr2.velocity = astr2_vec * 1.2
