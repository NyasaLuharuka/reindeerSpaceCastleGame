import pygame
import random
import time
pygame.init()
pygame.display.set_caption("Reindeer Space Castle Golf Ball")


run = True
WIDTH = 900
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
GOLF_BALLS = 7

reindeer = pygame.image.load("/Users/nyasa/Desktop/pygame/reindeer.png")
reindeer = pygame.transform.scale(reindeer, (75, 75))
castle = pygame.image.load("/Users/nyasa/Desktop/pygame/castle.png")
#find a longer castle
castle = pygame.transform.scale(castle, (150, 150))
background = pygame.image.load("/Users/nyasa/Desktop/pygame/background.jpeg")
golf_ball = pygame.image.load("/Users/nyasa/Desktop/pygame/golf_ball.png")
golf_ball = pygame.transform.scale(golf_ball, (30, 30))
bullet_img = pygame.image.load("/Users/nyasa/Desktop/pygame/bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (40, 20))

reindeer_rect = pygame.Rect(150, HEIGHT//2-30, 75, 75)
castle_rect = pygame.Rect(0, HEIGHT//2-100, 150, 150)
#make golf ball appear randomly
golf_ball_rect = pygame.Rect(800, random.randint(200, 400), 30, 30)

#create projectiles and projectile list

HEALTH = 3
def castle_health():
	global HEALTH
	global run
	if HEALTH <=0 :
		print("GAME OVER")
		run = False
	elif pygame.Rect.colliderect(golf_ball_rect, castle_rect):
		HEALTH -=1
		print(HEALTH)
		golf_ball_rect.x = 800
		golf_ball_rect.y = random.randint(50, 450)
		golf_ball_move()

def golf_ball_move():
	if golf_ball_rect.x>0:
		golf_ball_rect.x-=5
	else:
		golf_ball_rect.x = 800
		golf_ball_rect.y = random.randint(50, 450)
		golf_ball_move()

def reindeer_health():
	if pygame.Rect.colliderect(reindeer_rect, golf_ball_rect):
		pass
		#figure out how to stop reindeer if hit

def key_input(get_pressed):
	if pygame.key.get_pressed()[pygame.K_w] and reindeer_rect.y > 0:
		reindeer_rect.y -=5
	if pygame.key.get_pressed()[pygame.K_s] and reindeer_rect.y < HEIGHT-75:
		reindeer_rect.y +=5
	if pygame.key.get_pressed()[pygame.K_d] and reindeer_rect.x < WIDTH-75:
		reindeer_rect.x +=5
	if pygame.key.get_pressed()[pygame.K_a] and reindeer_rect.x > 0:
		reindeer_rect.x -=5

def handle_bullets(bullets):
	for bullet in bullets:
		bullet.x+=7
		if pygame.Rect.colliderect(golf_ball_rect, bullet):
			bullets.remove(bullet)
			golf_ball_rect.x = 800
			golf_ball_rect.y = random.randint(50, 450)
			golf_ball_move()
		elif bullet.x > WIDTH:
			bullets.remove(bullet)

def update_display(bullets):
	WINDOW.fill(WHITE)
	WINDOW.blit(background, (0, 0))
	WINDOW.blit(castle, (castle_rect.x, castle_rect.y))
	WINDOW.blit(reindeer, (reindeer_rect.x, reindeer_rect.y))
	WINDOW.blit(golf_ball, (golf_ball_rect.x, golf_ball_rect.y))
	for bullet in bullets:
		WINDOW.blit(bullet_img, (bullet.x, bullet.y))
	pygame.display.update()

def main():
	golf_ball_list = []
	bullets = []
	global run

	clock = pygame.time.Clock()
	run = True
	while run == True:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN and len(bullets)<=3:
				if event.key == pygame.K_SPACE:
					bullet = pygame.Rect(reindeer_rect.x +reindeer_rect.width, reindeer_rect.y+reindeer_rect.height//2, 40, 20)
					bullets.append(bullet)


		get_pressed = pygame.key.get_pressed()
		key_input(get_pressed)
		castle_health()
		reindeer_health()
		golf_ball_move()
		handle_bullets(bullets)
		update_display(bullets)

	pygame.quit()


if __name__ == "__main__":
	main()