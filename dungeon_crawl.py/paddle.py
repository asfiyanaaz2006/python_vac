# Setup
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Paddle Ball Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Game objects
ball = pygame.Rect(200, 200, 15, 15)
paddle = pygame.Rect(170, 380, 60, 10)
speed = [2, -2]  # Start slow

# State variables
score = 0
lives = 3
hit_counter = 0
next_speed_increase = 100  # first threshold
increment = 50  # increase threshold after each speedup

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 5
    if keys[pygame.K_RIGHT] and paddle.right < 400:
        pa…
