from pygame import *


class GameSprite(sprite.Sprite):
    
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
 
class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
 
    def update(self):
            keys = key.get_pressed()
            if keys[K_w] and self.rect.x > 5:
                self.rect.x -= self.speed
            if keys[K_s] and self.rect.x < win_width - 80:
                self.rect.x += self.speed

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket_1 = Player('racket.png', 30, 200, 4, 50, 150)
racket_r = Player('racket.png', 520, 200, 4, 50, 150) 
ball = Player('tennis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose_1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose_к = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get()
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fiil(back)
        racket_1.update_1()
        racket_r.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collides_rect(racket_1, ball) or sprite.collides_rect(racket_r, ball)
            speed_x *- -1
            speed_y *- 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            finish = True
            window.blit(lose_1, (200,200))
            game_over = True
        if ball.rect.y > win_width:
            finish = True
            window.blit(lose_1, (200,200))
            game_over = True

        racket_1.reset
        racket_r.reset
        ball.reset

    display.update()
    clock.ti
        