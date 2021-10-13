import pygame
import sys

pygame.init()
# 화면 타이틀 설정
pygame.display.set_caption("야마다상의 마네키네코 탈환 작전 Level 1")
# 화면 크기 설정
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 360
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# FPS
clock = pygame.time.Clock()
# 배경 만들기
img_bg = pygame.image.load("image/back1.png")
# 캐릭터 만들기
img_char = pygame.image.load("image/mychr4.png")
char = img_char.get_rect(centerx= SCREEN_WIDTH // 2.5, bottom= SCREEN_HEIGHT)
 
# creating a running loop(움직이기 반복문)
while True:
    screen.blit(img_bg, (0, 0))
       
    # creating a loop to check events that are occuring
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
         
        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:
               
            # 방향 키 ; 위
            if event.key == pygame.KEYUP:
                char.up += 5
               
            # 방향 키 ; 오른쪽
            if event.key == pygame.K_RIGHT:
                char.right += 5
                
            # 방향 키 ; 왼쪽
            if event.key == pygame.K_LEFT:
                char.left -= 5
                

    screen.blit(img_char, char)

    pygame.display.update()
    clock.tick(30)

pygame.quit()