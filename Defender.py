import pygame
import random

# تهيئة Pygame
pygame.init()
# تهيئة الصوت
pygame.mixer.init()
collision_sound = pygame.mixer.Sound("collision.wav")  # استبدل "collision.wav" بمسار ملف الصوت

# إعداد الشاشة
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Defender Game")

# الألوان
white = (255, 255, 255)

# تحميل الصور
player_img = pygame.image.load("player.png")  # استبدل "player.png" بمسار صورتك
enemy_img = pygame.image.load("enemy.png")    # استبدل "enemy.png" بمسار صورتك
bullet_img = pygame.image.load("bullet.png")   # استبدل "bullet.png" بمسار صورتك

# إعداد اللاعب
player_rect = player_img.get_rect()
player_rect.x = width // 2 - player_rect.width // 2
player_rect.y = height - player_rect.height
player_speed = 5

# إعداد الأعداء
enemy_speed = 3
enemies = []

def create_enemy():
    enemy_rect = enemy_img.get_rect()
    enemy_rect.x = random.randint(0, width - enemy_rect.width)
    enemy_rect.y = 0
    enemies.append(enemy_rect)

# إعداد الطلقات
bullet_speed = 7
bullets = []

def fire_bullet():
    bullet_rect = bullet_img.get_rect()
    bullet_rect.x = player_rect.x + player_rect.width // 2 - bullet_rect.width // 2
    bullet_rect.y = player_rect.y
    bullets.append(bullet_rect)

# حلقة اللعبة
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire_bullet()

    # تحريك اللاعب
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.x < width - player_rect.width:
        player_rect.x += player_speed

    # تحريك الأعداء
    if random.randint(0, 100) < 2:
        create_enemy()

    for enemy_rect in enemies:
        enemy_rect.y += enemy_speed
        if enemy_rect.y > height:
            enemies.remove(enemy_rect)

    # تحريك الطلقات
    for bullet_rect in bullets:
        bullet_rect.y -= bullet_speed
        if bullet_rect.y < 0:
            #collision_sound.play()
            bullets.remove(bullet_rect)
            #collision_sound.play()  # تشغيل صوت التصادم
    # التحقق من التصادم
    for enemy_rect in enemies:
        if player_rect.colliderect(enemy_rect):
           
           running = False

        for bullet_rect in bullets:
            if enemy_rect.colliderect(bullet_rect):
                enemies.remove(enemy_rect)
                if bullet_rect in bullets:
                    bullets.remove(bullet_rect)
                    collision_sound.play()
    # الرسم
    screen.fill(white)
    screen.blit(player_img, player_rect)

    for enemy_rect in enemies:
        screen.blit(enemy_img, enemy_rect)

    for bullet_rect in bullets:
        screen.blit(bullet_img, bullet_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
