import os
import pygame

dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    """A pygame sprite object for the player character.

    Attributes:
        image: The image file for the sprite.
        rect = The rectangular area that the sprite occupies. Size is based on the image.
        rect.x = Coordinate of the rectangle on the x-axis.
        rect.y = Coordinate of the rectangle on the y-axis.
        jumping = Boolean indicating whether the player is jumping or not.
        jump_height = Height of the player's jump.
        jump_velocity = Velocity of the player's jump.
        max_jump_bonus = A "bonus" to the jump height. The bonus is applied if 
        the key is held down.
        jump_counter = Controls the jump height bonus; when this equals the 
        maximum, the jump goes no higher.
        jump_gravity = Substracted from the jump velocity on each jumping frame.

    Args:
        pygame.sprite.Sprite: A pygame sprite.
    """

    def __init__(self, position):
        """Creates a new Player instance.

        Args:
            position ((int, int)): A tuple with the sprite's positional coordinates.
        """
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "small_dude.png")
        )

        self.rect = self.image.get_rect()

        self.rect.x = position[0]
        self.rect.y = position[1]

        self.jumping = False
        self.jump_height = 14
        self.jump_velocity = self.jump_height
        self.max_jump_bonus = 8
        self.jump_counter = 0
        self.jump_gravity = 1

    def get_position(self):
        """Returns the sprite's position.

        Returns:
            tuple: A tuple of two integers, the x coordinate and the y coordinate.
        """
        return (self.rect.x, self.rect.y)

    def is_jumping(self):
        """Returns True if the sprite is jumping.

        Returns:
            boolean: True if the sprite is jumping, False if not.
        """
        if self.jumping:
            return True

        return False

    def reset_jumping(self):
        """Resets the values related to jumping. 
        """
        self.jumping = False
        self.jump_height = 14
        self.jump_velocity = self.jump_height
        self.jump_counter = 0
