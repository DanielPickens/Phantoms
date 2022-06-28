import pygame
import random

class Trail(pygame.sprite.Sprite):
	def __init__(self, pos, color, win):
		super(Trail, self).__init__()
		self.color = color
		self.win = win

		self.x, self.y = pos
		self.y += 10
		self.dx = random.randint(0,20) / 10 - 1
		self.dy = -2
		self.size = random.randint(4,7)

		self.rect = pygame.draw.circle(self.win, self.color, (self.x, self.y), self.size)

	def update(self):
		self.x -= self.dx
		self.y -= self.dy
		self.size -= 0.1

		if self.size <= 0:
			self.kill()

		self.rect = pygame.draw.circle(self.win, self.color, (self.x, self.y), self.size)
	
class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y, win):
		super(Explosion, self).__init__()
		self.x = x
		self.y = y
		self.win = win

		self.size = random.randint(4,9)
		self.life = 40
		self.lifetime = 0

		self.x_vel = random.randrange(-4, 4)
		self.y_vel = random.randrange(-4, 4)
		
		self.color = 150
			
	def update (self, screen_scroll):
		self.size -= 0.2
		self.lifetime += 1
		self.color -= 2
		if self.lifetime <= self.life:
			self.x += self.x_vel + screen_scroll
			self.y += self.y_vel
			s = int(self.size)
			pygame.draw.rect(self.win, (self.color, self.color, self.color), (self.x, self.y,s,s))
		else:
			self.kill()

class DustExplosion(pygame.sprite.Sprite):
	def __init__(self, x, y, win):
		super(DustExplosion, self).__init__()
		self.x = x
		self.y = y
		self.win = win

		self.size = random.randint(4,9)
		self.life = 40
		self.lifetime = 0

		self.x_vel = random.randrange(-4, 4)
		self.y_vel = random.randrange(-4, 4)
		
		self.color = 150
			
	def update (self, screen_scroll):
		self.size -= 0.2
		self.lifetime += 1
		self.color -= 2
		if self.lifetime <= self.life:
			self.x += self.x_vel + screen_scroll
			self.y += self.y_vel
			s = int(self.size)
			pygame.draw.rect(self.win, (self.color, self.color, self.color), (self.x, self.y,s,s))
		else:
			self.kill()

class Particle(pygame.sprite.Sprite):
	def __init__(self, x, y, win):
		super(Particle, self).__init__()
		self.x = x
		self.y = y
		self.win = win

		self.size = random.randint(4,9)
		self.life = 40
		self.lifetime = 0

		self.x_vel = random.randrange(-4, 4)
		self.y_vel = random.randrange(-4, 4)
		
		self.color = 150
			
	def update (self, screen_scroll):
		self.size -= 0.2
		self.lifetime += 1
		self.color -= 2
		if self.lifetime <= self.life:
			self.x += self.x_vel + screen_scroll
			self.y += self.y_vel
			s = int(self.size)
			pygame.draw.rect(self.win, (self.color, self.color, self.color), (self.x, self.y,s,s))
		else:
			self.kill()

class Particle_2(pygame.sprite.Sprite):
	def __init__(self, x, y, win):
		super(Particle_2, self).__init__()
		self.x = x
		self.y = y
		self.win = win

		self.size = random.randint(4,9)
		self.life = 40
		self.lifetime = 0

		self.x_vel = random.randrange(-4, 4)
		self.y_vel = random.randrange(-4, 4)


		self.color = 150

	def update (self, screen_scroll):
		self.size -= 0.2
		self.lifetime += 1
		self.color -= 2
		if self.lifetime <= self.life:
			self.x += self.x_vel + screen_scroll
			self.y += self.y_vel
			s = int(self.size)

			pygame.draw.rect(self.win, (self.color, self.color, self.color), (self.x, self.y,s,s))
		else:
			self.kill()

class Dust(pygame.sprite.Sprite):
	def __init__(self, x, y, win):
		super(Dust, self).__init__()
		self.x = x
		self.y = y
		self.win = win

		self.size = random.randint(4,9)
		self.life = 40
		self.lifetime = 0

		self.x_vel = random.randrange(-4, 4)
		self.y_vel = random.randrange(-4, 4)

		self.color = 150

	def update (self, screen_scroll):
		self.size -= 0.2
		self.lifetime += 1
		self.color -= 2
		if self.lifetime <= self.life:

			self.x += self.x_vel + screen_scroll
			self.y += self.y_vel
			s = int(self.size)

			pygame.draw.rect(self.win, (self.color, self.color, self.color), (self.x, self.y,s,s))
		else:
			self.kill()

class WaterDroplet(pygame.sprite.Sprite):
	def __init__(self, x, y, win):
		super(WaterDroplet, self).__init__()
		self.x = x
		self.y = y
		self.win = win

		self.size = random.randint(4,9)
		self.life = 40
		self.lifetime = 0

		self.x_vel = random.randrange(-4, 4)
		self.y_vel = random.randrange(-4, 4)

		self.color = 150

	def update (self, screen_scroll):
		self.size -= 0.2
		self.lifetime += 1
		self.color -= 2
		if self.lifetime <= self.life:

			self.x += self.x_vel + screen_scroll
			self.y += self.y_vel
			s = int(self.size)

			pygame.draw.rect(self.win, (self.color, self.color, self.color), (self.x, self.y,s,s))
		else:
			self.kill()

class Graupel(pygame.sprite.Sprite):
	def __init__(self, x, y, win):
		super(Graupel, self).__init__()
		self.x = x
		self.y = y
		self.win = win

		self.size = random.randint(4,9)
		self.life = 40
		self.lifetime = 0

		self.x_vel = random.randrange(-4, 4)
		self.y_vel = random.randrange(-4, 4)

		self.color = 150

	def update (self, screen_scroll):
		self.size -= 0.2
		self.lifetime += 1
		self.color -= 2
		if self.lifetime <= self.life:
			
			self.x += self.x_vel + screen_scroll
			self.y += self.y_vel
			s = int(self.size)

			pygame.draw.rect(self.win, (self.color, self.color, self.color), (self.x, self.y,s,s))
		else:

			self.kill()
			

				