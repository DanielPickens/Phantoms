import random
import pygame
from projectiles import Bullet

TILE_SIZE = 16

pygame.mixer.init()
bullet_fx = pygame.mixer.Sound('Sounds/ghost_shot.mp3')
#initializes ghost enemy class 
class Ghost(pygame.sprite.Sprite):
	def __init__(self, x, y, win):
		super(Ghost, self).__init__()

		self.x = x
		self.y = y
		self.win = win
		self.initial_pos_x = x

		self.size = 32

		self.walk_left = []
		self.walk_right = []
		self.hit_list = []
		self.death_list = []

		for i in range(1,6):
			image = pygame.image.load(f'Assets/Ghost/Enemywalk{i}.png') # declared variable calls ghost asset as a pass reference parameter argument 
			right = right = pygame.transform.scale(image, (self.size, self.size))
			left = pygame.transform.flip(right, True, False)
			self.walk_right.append(right)
			self.walk_left.append(left)
		for i in range(1, 3):
			image = pygame.image.load(f'Assets/Ghost/Enemyhit{i}.png')
			image = pygame.transform.scale(image, (self.size, self.size))
			self.hit_list.append(image)
		for i in range(1,9):
			image = pygame.image.load(f'Assets/Ghost/Enemydead{i}.png')
			image = pygame.transform.scale(image, (self.size, self.size))
			self.death_list.append(image)

		self.walk_index = 0
		self.death_index = 0
		self.hit_index = 0
		self.counter = 0

		self.dx = random.choice([-1, 1])
		self.alive = True
		self.health = 100
		self.hit = False
		self.on_death_bed = False

		self.image = self.walk_right[self.walk_index]
		self.rect = self.image.get_rect(center=(self.x, self.y))

	def update(self, screen_scroll, bullet_group, p):
		if self.health:
			self.rect.x += (self.dx + screen_scroll)
			self.x += screen_scroll
			if abs(self.rect.x - self.x) >= 2 * TILE_SIZE:
				self.dx *= -1

		if self.health <= 0:
			self.on_death_bed = True

		self.counter += 1
		if self.counter % 5 == 0:
			if self.on_death_bed:
				self.death_index += 1
				if self.death_index >= len(self.death_list):
					self.kill()
					self.alive = False
			if self.hit:
				self.hit_index += 1
				if self.hit_index >= len(self.hit_list):
					self.hit_index = 0
					self.hit = False
			else:
				self.walk_index  = (self.walk_index + 1) % len(self.walk_left)
				
		if self.counter % 50 == 0:
			if self.health > 0 and (abs(p.rect.x - self.rect.x) <= 200):
				x, y = self.rect.center
				direction = self.dx
				bullet = Bullet(x, y, direction, (160, 160, 160), 2, self.win)
				bullet_group.add(bullet)
				bullet_fx.play()

		if self.alive:
			if self.on_death_bed:
				self.image = self.death_list[self.death_index]
			elif self.hit:
				self.image = self.hit_list[self.hit_index]
			else:
				if self.dx == -1:
					self.image = self.walk_left[self.walk_index]
				elif self.dx == 1:
					self.image = self.walk_right[self.walk_index]

	def draw(self, win):
		win.blit(self.image, self.rect)

class Goblin(pygame.sprite.Sprite):
	def __init__(self, x, y, win):
		super(Goblin, self).__init__()

		self.x = x
		self.y = y
		self.win = win
		self.initial_pos_x = x

		self.size = 32

		self.walk_left = []
		self.walk_right = []
		self.hit_list = []
		self.death_list = []

		for i in range(1,6):

			image = pygame.image.load(f'Assets/Goblin/Enemywalk{i}.png')
			right = right = pygame.transform.scale(image, (self.size, self.size))
			left = pygame.transform.flip(right, True, False)
			self.walk_right.append(right)
			self.walk_left.append(left)
		for i in range(1, 3):

			image = pygame.image.load(f'Assets/Goblin/Enemyhit{i}.png')
			image = pygame.transform.scale(image, (self.size, self.size))
			self.hit_list.append(image)
		for i in range(1,9):

			image = pygame.image.load(f'Assets/Goblin/Enemydead{i}.png')

			image = pygame.transform.scale(image, (self.size, self.size))
			self.death_list.append(image)

		self.walk_index = 0
		self.death_index = 0
		self.hit_index = 0
		self.counter = 0

		self.dx = random.choice([-1, 1])
		self.alive = True
		self.health = 100
		self.hit = False
		self.on_death_bed = False

		self.image = self.walk_right[self.walk_index]
		self.rect = self.image.get_rect(center=(self.x, self.y))

	def update(self, screen_scroll, bullet_group, p):
		if self.health:
			self.rect.x += (self.dx + screen_scroll)

			self.x += screen_scroll
			if abs(self.rect.x - self.x) >= 2 * TILE_SIZE:
				self.dx *= -1

		if self.health <= 0:

			self.on_death_bed = True

		self.counter += 1
		if self.counter % 5 == 0:
			if self.on_death_bed:
				self.death_index += 1
				if self.death_index >= len(self.death_list):
					self.kill()
					self.alive = False
			if self.hit:
				self.hit_index += 1
				if self.hit_index >= len(self.hit_list):
					self.hit_index = 0
					self.hit = False
			else:
				self.walk_index  = (self.walk_index + 1) % len(self.walk_left)

		if self.counter % 50 == 0:
			if self.health > 0 and (abs(p.rect.x - self.rect.x) <= 200):
				x, y = self.rect.center
				direction = self.dx
				bullet = Bullet(x, y, direction, (160, 160, 160), 2, self.win)
				bullet_group.add(bullet)
				bullet_fx.play()

		if self.alive:
			if self.on_death_bed:
				self.image = self.death_list[self.death_index]
			elif self.hit:
				self.image = self.hit_list[self.hit_index]
			else:
				if self.dx == -1:
					self.image = self.walk_left[self.walk_index]
				elif self.dx == 1:

					self.image = self.walk_right[self.walk_index]

	def draw(self, win):
		win.blit(self.image, self.rect)



class Zombie(pygame.sprite.Sprite):
	def __init__(self, x, y, win):
		super(Zombie, self).__init__()

		self.x = x
		self.y = y
		self.win = win
		self.initial_pos_x = x

		self.size = 32

		self.walk_left = []
		self.walk_right = []
		self.hit_list = []
		self.death_list = []

		for i in range(1,6):

			image = pygame.image.load(f'Assets/Zombie/Enemywalk{i}.png')
			right = right = pygame.transform.scale(image, (self.size, self.size))
			left = pygame.transform.flip(right, True, False)
			self.walk_right.append(right)
			self.walk_left.append(left)
		for i in range(1, 3):

			image = pygame.image.load(f'Assets/Zombie/Enemyhit{i}.png')
			image = pygame.transform.scale(image, (self.size, self.size))
			self.hit_list.append(image)
		for i in range(1,9):

			image = pygame.image.load(f'Assets/Zombie/Enemydead{i}.png')

			image = pygame.transform.scale(image, (self.size, self.size))
			self.death_list.append(image)

		self.walk_index = 0
		self.death_index = 0
		self.hit_index = 0
		self.counter = 0

		self.dx = random.choice([-1, 1])
		self.alive = True
		self.health = 100
		self.hit = False
		self.on_death_bed = False

		self.image = self.walk_right[self.walk_index]
		self.rect = self.image.get_rect(center=(self.x, self.y))

	def update(self, screen_scroll, bullet_group, p):
		if self.health:
			self.rect.x += (self.dx + screen_scroll)

			self.x += screen_scroll
			if abs(self.rect.x - self.x) >= 2 * TILE_SIZE:
				self.dx *= -1

		if self.health <= 0:

			self.on_death_bed = True

		self.counter += 1
		if self.counter % 5 == 0:
			if self.on_death_bed:
				self.death_index += 1
				if self.death_index >= len(self.death_list):
					self.kill()
					self.alive = False
			if self.hit:
				self.hit_index += 1
				if self.hit_index >= len(self.hit_list):
					self.hit_index = 0
					self.hit = False
			else:
				self.walk_index  = (self.walk_index + 1) % len(self.walk_left)

		if self.counter % 50 == 0:
			if self.health > 0 and (abs(p.rect.x - self.rect.x) <= 200):
				x, y = self.rect.center
				direction = self.dx
				bullet = Bullet(x, y, direction, (160, 160, 160), 2, self.win)
				bullet_group.add(bullet)
				bullet_fx.play()

		if self.alive:
			if self.on_death_bed:
				self.image = self.death_list[self.death_index]
			elif self.hit:
				self.image = self.hit_list[self.hit_index]
			else:
				if self.dx == -1:
					self.image = self.walk_left[self.walk_index]
				elif self.dx == 1:

					self.image = self.walk_right[self.walk_index]

	def draw(self, win):
		win.blit(self.image, self.rect)
	# checks if the zombie is hit by a bullet and if so, reduces the zombie's health accordinging to the bullet's damage rate
	def check_collision(self, p):
		if self.alive:
			if self.rect.colliderect(p.rect):
				p.health -= 10
				self.hit = True
				return True
			else:
				return False
		else:
			return False
	
# 	def check_bullet_collision(self, bullet_group):
# 		if self.alive:
# 			for bullet in bullet_group:
# 				if self.rect.colliderect(bullet.rect):
# 					self.health -= bullet.damage
# 					bullet.kill()
# 					self.hit = True
# 					return True
# 			return False
# 		else:
# 			return False

# class Bullet(pygame.sprite.Sprite):
# 	def __init__(self, x, y, direction, color, speed, win):
# 		super(Bullet, self).__init__()

# 		self.x = x
# 		self.y = y
# 		self.direction = direction
# 		self.color = color
# 		self.speed = speed
# 		self.win = win

# 		self.image = pygame.Surface((5, 5))
# 		self.image.fill(self.color)
# 		self.rect = self.image.get_rect(center=(self.x, self.y))

# 	def update(self, screen_scroll):
# 		self.rect.x += (self.direction * self.speed) + screen_scroll

# 	def draw(self, win):
# 		win.blit(self.image, self.rect)


# 	class EnemyCollisionChecks(pygame.sprite.Sprite):
# 		def __init__(self, enemy_group, bullet_group, p):
# 			super(EnemyCollisionChecks, self).__init__()
# 			self.enemy_group = enemy_group
# 			self.bullet_group = bullet_group
# 			self.p = p

# 		def update(self, screen_scroll):
# 			for enemy in self.enemy_group:
# 				enemy.check_collision(self.p)
# 				enemy.check_bullet_collision(self.bullet_group)
# 				enemy.update(screen_scroll, self.bullet_group, self.p)