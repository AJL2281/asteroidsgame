import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def update(self, dt):
        pass

    def collision(self, circle):
        distance = pygame.math.Vector2.distance_to(self.position, circle.position)

        if distance > (self.radius + circle.radius):
            return False
        else:
            return True