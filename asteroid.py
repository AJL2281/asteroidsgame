import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position +=  self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return self.kill()

        random_angle = random.uniform(20, 50)

        vector1_split = self.velocity.rotate(random_angle) * 1.2
        vector2_split = self.velocity.rotate(-random_angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_a.velocity = vector1_split
        asteroid_b.velocity = vector2_split

        self.kill()