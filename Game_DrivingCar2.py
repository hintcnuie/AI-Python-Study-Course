import pygame
import random
import sys

# 初始化Pygame
pygame.init()

# -------------------------- 游戏基础设置 --------------------------
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("卡通汽车驾驶游戏")
clock = pygame.time.Clock()
FPS = 60

# 颜色定义
ROAD_COLOR = (50, 50, 50)  # 道路灰色
LINE_COLOR = (255, 255, 255)  # 道路白线
SKY_COLOR = (135, 206, 235)  # 天空蓝色
GREEN = (34, 139, 34)  # 树木绿色
WHITE = (255, 255, 255)
YELLOW = (255, 223, 0)

# -------------------------- 游戏元素参数 --------------------------
# 道路参数
road_width = 400
road_x = (WIDTH - road_width) // 2
road_scroll = 0
line_height = 40
line_gap = 20

# 汽车参数
car_width = 60
car_height = 100
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 30
car_speed = 8

# 场景元素（大楼、树木、路灯）
buildings = []
trees = []
street_lights = []
element_scroll = 0


# 生成路边元素
def generate_scenery():
    # 清空旧元素
    buildings.clear()
    trees.clear()
    street_lights.clear()

    # 左侧元素
    for i in range(8):
        # 大楼
        buildings.append({
            "x": random.randint(20, road_x - 40),
            "y": -i * 120,
            "width": random.randint(40, 70),
            "height": random.randint(80, 150),
            "color": (random.randint(100, 200), random.randint(100, 200), random.randint(150, 220))
        })
        # 树木
        trees.append({
            "x": random.randint(20, road_x - 30),
            "y": -i * 100,
            "size": random.randint(20, 35)
        })
        # 路灯
        if i % 2 == 0:
            street_lights.append({
                "x": random.randint(road_x - 30, road_x - 10),
                "y": -i * 150
            })

    # 右侧元素
    for i in range(8):
        # 大楼
        buildings.append({
            "x": random.randint(road_x + road_width + 20, WIDTH - 60),
            "y": -i * 120,
            "width": random.randint(40, 70),
            "height": random.randint(80, 150),
            "color": (random.randint(100, 200), random.randint(100, 200), random.randint(150, 220))
        })
        # 树木
        trees.append({
            "x": random.randint(road_x + road_width + 10, WIDTH - 40),
            "y": -i * 100,
            "size": random.randint(20, 35)
        })
        # 路灯
        if i % 2 == 0:
            street_lights.append({
                "x": random.randint(road_x + road_width + 10, road_x + road_width + 30),
                "y": -i * 150
            })


# 初始生成场景
generate_scenery()


# -------------------------- 绘制函数 --------------------------
# 绘制卡通汽车
def draw_car(x, y):
    # 车身主体（卡通蓝色）
    pygame.draw.rect(screen, (0, 191, 255), (x, y, car_width, car_height))
    # 车顶
    pygame.draw.rect(screen, (0, 150, 200), (x + 10, y + 20, car_width - 20, 40))
    # 车轮
    pygame.draw.circle(screen, (30, 30, 30), (x + 12, y + car_height), 10)
    pygame.draw.circle(screen, (30, 30, 30), (x + car_width - 12, y + car_height), 10)
    pygame.draw.circle(screen, (30, 30, 30), (x + 12, y + 10), 8)
    pygame.draw.circle(screen, (30, 30, 30), (x + car_width - 12, y + 10), 8)
    # 车窗
    pygame.draw.rect(screen, (200, 230, 255), (x + 15, y + 25, car_width - 30, 30))


# 绘制道路
def draw_road(scroll):
    # 主道路
    pygame.draw.rect(screen, ROAD_COLOR, (road_x, 0, road_width, HEIGHT))
    # 道路中线（滚动效果）
    for y in range(-line_height, HEIGHT, line_height + line_gap):
        pygame.draw.rect(screen, LINE_COLOR,
                         (WIDTH // 2 - 5, y + scroll, 10, line_height))


# 绘制大楼
def draw_buildings(scroll):
    for b in buildings:
        pygame.draw.rect(screen, b["color"],
                         (b["x"], b["y"] + scroll, b["width"], b["height"]))
        # 窗户
        for wx in range(5, b["width"], 15):
            for wy in range(10, b["height"], 25):
                pygame.draw.rect(screen, YELLOW,
                                 (b["x"] + wx, b["y"] + scroll + wy, 8, 12))


# 绘制树木
def draw_trees(scroll):
    for t in trees:
        # 树干
        pygame.draw.rect(screen, (139, 69, 19),
                         (t["x"] - 5, t["y"] + scroll + t["size"], 10, t["size"]))
        # 树冠
        pygame.draw.circle(screen, GREEN, (t["x"], t["y"] + scroll), t["size"])
        pygame.draw.circle(screen, (0, 200, 0), (t["x"], t["y"] + scroll - 10), t["size"] - 8)


# 绘制路灯
def draw_lights(scroll):
    for l in street_lights:
        # 灯杆
        pygame.draw.rect(screen, (100, 100, 100),
                         (l["x"], l["y"] + scroll, 4, 60))
        # 灯罩
        pygame.draw.circle(screen, YELLOW, (l["x"] + 2, l["y"] + scroll + 10), 8)


# 绘制操作提示
def draw_hints():
    font = pygame.font.SysFont(None, 36)
    text = font.render("← 左键  |  右键 →", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 120, 20))


# -------------------------- 游戏主循环 --------------------------
running = True
while running:
    # 背景填充
    screen.fill(SKY_COLOR)

    # 事件监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 汽车控制（左右方向键）
    keys = pygame.key.get_pressed()
    ## 判断按下的是左键还是右键，
    ## Todo 判断按下的是左键，而且汽车不要超过道路左侧
    if keys[pygame.K_LEFT] and car_x > road_x:
        car_x -= car_speed
    ## Todo 判断按下的是右键，而且汽车不要超过道路右侧
    if keys[pygame.K_RIGHT] and car_x < road_x + road_width - car_width:
        car_x += car_speed

    # 滚动效果（营造前进感）
    road_scroll += 5
    element_scroll += 5
    if road_scroll >= line_height + line_gap:
        road_scroll = 0
    if element_scroll >= 150:
        generate_scenery()
        element_scroll = 0

    # 绘制所有元素
    draw_buildings(element_scroll)
    draw_trees(element_scroll)
    draw_lights(element_scroll)
    draw_road(road_scroll)
    draw_car(car_x, car_y)
    draw_hints()

    # 更新屏幕
    pygame.display.flip()
    clock.tick(FPS)

# 退出游戏
pygame.quit()
sys.exit()