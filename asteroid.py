from circleshape import *
from constants import *
import pygame
from logger import *
import random

class Asteroid(CircleShape):
  def __init__(self, x: float, y: float, radius: float) -> None:
      super().__init__(x, y, radius)

  def draw(self, screen: pygame.Surface) -> None:
      pygame.draw.circle(screen, "white", self.position, self.radius, width = LINE_WIDTH,)
        
  def update(self, dt: float) -> None:
      
      
      self.position += self.velocity * dt 

  def split(self,):
    self.kill()  
    if self.radius <= ASTEROID_MIN_RADIUS:
         
        return
    else:
        log_event("asteroid_split")
        respawn_angle = random.uniform(20, 50)
        new_direction_plus = self.velocity.rotate(respawn_angle)
        new_direction_minus = self.velocity.rotate(respawn_angle * -1) 
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        
        split_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_1.velocity = new_direction_plus * 1.2
        split_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_2.velocity = new_direction_minus * 1.2    


       