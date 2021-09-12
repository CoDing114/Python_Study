import pygame

pygame.init()   # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
pygame.display.set_mode((screen_width, screen_height))   # 화면 크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("Rilla Game")  # 게임 이름

# 이벤트 루프
running = True  # 게임이 진행중인가 확인
while running:
    for event in pygame.event.get():    # pygame을 쓰기위해 무조건 적어야하는 부분
        if event.type == pygame.QUIT:   # 차이이 닫히는 이벤트가 발생하였는가?
            running = False             # 게임이 진행중이 아님

# pygame 종료
pygame.quit()
