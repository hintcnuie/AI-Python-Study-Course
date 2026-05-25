import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("卡通汽车驾驶-超车挑战")
clock = pygame.time.Clock()
FPS = 60

# 颜色常量
ROAD_COLOR = (50, 50, 50)
SKY_COLOR = (135, 206, 235)
GREEN = (34, 139, 34)
WHITE = (255, 255, 255)
YELLOW = (255, 223, 0)
RED = (255, 0, 0)
ENEMY_CAR_COLOR = (220, 80, 80)
SCORE_COLOR = (255, 210, 0)
SCORE_BG = (20, 20, 20)

# 道路车道配置
road_width = 400
road_x = (WIDTH - road_width) // 2
lane_count = 3
lane_width = road_width // lane_count

# 车辆尺寸与速度设置
car_w, car_h = 60, 100
base_speed = 4
current_speed = 4
max_speed = 12
speed_step = 1
enemy_speed = 4

# 游戏状态
score = 0
game_over = False

# 中文适配字体
try:
    font = pygame.font.Font("simhei.ttf", 48)
except:
    try:
        font = pygame.font.Font("Microsoft YaHei.ttf", 48)
    except:
        font = pygame.font.SysFont("simsun", 48)

# 车辆列表
enemy_cars = []
spawn_timer = 0
spawn_gap = 120

# 场景滚动
road_scroll = 0
element_scroll = 0
buildings = []
trees = []
street_lights = []

# 重置游戏
def reset_game():
    global score, game_over, spawn_timer, enemy_cars, car_x, current_speed
    score = 0
    game_over = False
    spawn_timer = 0
    enemy_cars.clear()
    current_speed = base_speed
    mid_lane_x = road_x + lane_width + (lane_width - car_w) // 2
    car_x = mid_lane_x

car_x = road_x + lane_width + (lane_width - car_w) // 2
car_y = HEIGHT - car_h - 30

# 生成路边场景
def generate_scenery():
    buildings.clear()
    trees.clear()
    street_lights.clear()
    for i in range(8):
        buildings.append({"x":random.randint(20, road_x-40),"y":-i*120,"w":random.randint(40,70),"h":random.randint(80,150),"c":(random.randint(100,200),random.randint(100,200),random.randint(150,220))})
        trees.append({"x":random.randint(20,road_x-30),"y":-i*100,"size":random.randint(20,35)})
        if i%2==0:
            street_lights.append({"x":random.randint(road_x-30,road_x-10),"y":-i*150})
    for i in range(8):
        buildings.append({"x":random.randint(road_x+road_width+20,WIDTH-60),"y":-i*120,"w":random.randint(40,70),"h":random.randint(80,150),"c":(random.randint(100,200),random.randint(100,200),random.randint(150,220))})
        trees.append({"x":random.randint(road_x+road_width+10,WIDTH-40),"y":-i*100,"size":random.randint(20,35)})
        if i%2==0:
            street_lights.append({"x":random.randint(road_x+road_width+10,road_x+road_width+30),"y":-i*150})

# 固定车道生成障碍车
def spawn_enemy():
    lane_idx = random.randint(0, lane_count-1)
    lane_center_x = road_x + lane_idx * lane_width + (lane_width - car_w) // 2
    enemy_cars.append({
        "x": lane_center_x,
        "y": -car_h,
        "w": car_w,
        "h": car_h,
        "scored": False
    })

# 碰撞检测
def collide(rect1, rect2):
    return rect1.colliderect(rect2)

# 绘制玩家车
def draw_player_car(x, y):
    pygame.draw.rect(screen, (0, 191, 255), (x, y, car_w, car_h))
    pygame.draw.rect(screen, (0, 150, 200), (x+10, y+20, car_w-20, 40))
    pygame.draw.circle(screen, (30,30,30), (x+12, y+car_h), 10)
    pygame.draw.circle(screen, (30,30,30), (x+car_w-12, y+car_h), 10)
    pygame.draw.circle(screen, (30,30,30), (x+12, y+10), 8)
    pygame.draw.circle(screen, (30,30,30), (x+car_w-12, y+10), 8)
    pygame.draw.rect(screen, (200,230,255), (x+15, y+25, car_w-30, 30))

# 绘制障碍车
def draw_enemy():
    for car in enemy_cars:
        x,y,w,h = car["x"],car["y"],car["w"],car["h"]
        pygame.draw.rect(screen, ENEMY_CAR_COLOR, (x,y,w,h))
        pygame.draw.rect(screen, (180,50,50), (x+8,y+18,w-16,35))
        pygame.draw.circle(screen, (20,20,20), (x+10,y+h),9)
        pygame.draw.circle(screen, (20,20,20), (x+w-10,y+h),9)

# 绘制道路
def draw_road():
    pygame.draw.rect(screen, ROAD_COLOR, (road_x,0,road_width,HEIGHT))
    for i in range(1, lane_count):
        split_x = road_x + i * lane_width
        pygame.draw.line(screen, (80,80,80), (split_x,0), (split_x,HEIGHT), 2)

def draw_build(scroll):
    for b in buildings:
        pygame.draw.rect(screen, b["c"], (b["x"], b["y"]+scroll, b["w"], b["h"]))
        for wx in range(5,b["w"],15):
            for wy in range(10,b["h"],25):
                pygame.draw.rect(screen,YELLOW,(b["x"]+wx,b["y"]+scroll+wy,8,12))

def draw_tree(scroll):
    for t in trees:
        pygame.draw.rect(screen,(139,69,19),(t["x"]-5,t["y"]+scroll+t["size"],10,t["size"]))
        pygame.draw.circle(screen,GREEN,(t["x"],t["y"]+scroll),t["size"])
        pygame.draw.circle(screen,(0,200,0),(t["x"],t["y"]+scroll-10),t["size"]-8)

def draw_light(scroll):
    for l in street_lights:
        pygame.draw.rect(screen,(100,100,100),(l["x"],l["y"]+scroll,4,60))
        pygame.draw.circle(screen,YELLOW,(l["x"]+2,l["y"]+scroll+10),8)

# UI界面
def draw_ui():
    score_text = font.render(f"得分：{score}", True, SCORE_COLOR)
    score_rect = score_text.get_rect(center=(WIDTH//2, 35))
    pygame.draw.rect(screen, SCORE_BG, score_rect.inflate(20,10))
    screen.blit(score_text, score_rect)

    speed_text = font.render(f"车速：{int(current_speed*10)}", True, WHITE)
    speed_rect = speed_text.get_rect(center=(WIDTH//2, 80))
    screen.blit(speed_text, speed_rect)

    hint_txt = font.render("左右变道 上加速 下减速", True, WHITE)
    hint_rect = hint_txt.get_rect(center=(WIDTH//2, 120))
    screen.blit(hint_txt, hint_rect)

    if game_over:
        over_txt = font.render("撞车啦！按任意键重新开始", True, RED)
        over_rect = over_txt.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(over_txt, over_rect)

generate_scenery()

# 主循环
while True:
    screen.fill(SKY_COLOR)
    event_list = pygame.event.get()
    for e in event_list:
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_over and e.type == pygame.KEYDOWN:
            reset_game()

    if not game_over:
        keys = pygame.key.get_pressed()
        # 左右变道
        if keys[pygame.K_LEFT] and car_x > road_x:
            car_x += -6
        if keys[pygame.K_RIGHT] and car_x < road_x + road_width - car_w:
            car_x += 6

        # 上键加速，下键减速，限制区间
        if keys[pygame.K_UP]:
            current_speed = min(current_speed + speed_step, max_speed)
        if keys[pygame.K_DOWN]:
            current_speed = max(current_speed - speed_step, 1)

        # 车辆生成
        spawn_timer += 1
        if spawn_timer >= spawn_gap:
            spawn_enemy()
            spawn_timer = 0

        # 车辆逻辑
        player_rect = pygame.Rect(car_x, car_y, car_w, car_h)
        del_list = []
        for idx, car in enumerate(enemy_cars):
            car["y"] += enemy_speed
            car_rect = pygame.Rect(car["x"], car["y"], car["w"], car["h"])
            if collide(player_rect, car_rect):
                game_over = True
            if not car["scored"] and car["y"] > car_y + car_h:
                car["scored"] = True
                score += 1
            if car["y"] > HEIGHT:
                del_list.append(idx)
        for idx in reversed(del_list):
            enemy_cars.pop(idx)

        # 场景滚动随当前车速变化
        road_scroll += current_speed
        element_scroll += current_speed
        if element_scroll >= 150:
            generate_scenery()
            element_scroll = 0

    draw_build(element_scroll)
    draw_tree(element_scroll)
    draw_light(element_scroll)
    draw_road()
    draw_enemy()
    draw_player_car(car_x, car_y)
    draw_ui()

    pygame.display.update()
    clock.tick(FPS)