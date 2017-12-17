import pygame, random, time  #Gotta Go Fast, created by Jerry Xu ─=≡Σᕕ( ͡° ͜ʖ ͡°)ᕗ
pygame.init()
#define stuff
screen = pygame.display.set_mode([800, 600])
amount = 5
x = [0]*amount
y = [0]*amount
speedx = [0]*amount
color = [0]*amount
clock = pygame.time.Clock()
BLACK = (0,0,0)
WHITE = (255,255,255)
lap = [0]*amount
y[0] = 480
y[1] = 390
y[2] = 300
y[3] = 210
y[4] = 120
distance = [0]*amount
speed_control = 20
MAX_SPEED_CONTROL = 120
MIN_SPEED_CONTROL = 10

#generate cars
for i in range(amount):
    distance[i] = 0
    lap[i] = 1
    x[i] = 0
    speedx[i] = random.randint(20, 25)
    color[i] = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
speedx[2] = 0
keepGoing = True
start_time = pygame.time.get_ticks()
#game loop
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
            pygame.quit()
    #elapsed time
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    #key pressed thing
    keys = pygame.key.get_pressed()
    #acceleration 
    if keys[pygame.K_a]:
        if speed_control < MAX_SPEED_CONTROL:
            speed_control += 1
    #deceleration 
    elif keys[pygame.K_d]:
        if speed_control > MIN_SPEED_CONTROL:
            speed_control -= 1
    #movement
    x[2] += int(speed_control * 4.875 * elapsed_time / 1000.0)
    #moving "natural" cars
    for i in range(amount):
        if i != 2:
            x[i] += speedx[i]
        if x[i] >= 800:
            x[i] -= 800
            lap[i] += 1
        #distance used to measure place laps (-1 because you start on 1) * 800 + x ─=≡Σᕕ( ͡° ͜ʖ ͡°)ᕗ
        distance[i] = (lap[i] - 1)*800 + x[i]
    #how many cars ahead of you, generate place 
    num_better = 0
    for i in range(amount):
        if distance[i] > distance[2]:
            num_better += 1
    place = num_better + 1
    #text: controls, lap #, place, time
    screen.fill(BLACK)
    string = ("Press [A] to accelerate, [D] to decelerate, and [Q] to quit. " \
             "You are controlling the car in the middle.")
    text = pygame.font.SysFont("Arial", 24).render(string, True, WHITE)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    stri = "You are on Lap #"
    stri += str(lap[2])
    stri += ". You are in "
    stri += str(place)
    if place == 1:
        stri += "st Place."
    elif place == 2:
        stri += "nd Place."
    elif place == 3:
        stri += "rd Place."
    else:
        stri += "th Place."
    #game over
    
    stri += " Time Left: " + str(20 - int(current_time / 1000)) + " seconds."
    text_two = pygame.font.SysFont("Arial", 24).render(stri, True, WHITE)
    textrect = text_two.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.y = 580
    screen.blit(text, text_rect)
    screen.blit(text_two, textrect)
    #draw cars
    for i in range(amount):
        pygame.draw.lines(screen, color[i], True, [(x[i]+10, y[i]-20), (x[i]+30, y[i]-10), (x[i]+40, y[i]-10), (x[i]+40, y[i]), (x[i]-30, y[i]), (x[i]-30, y[i]-10), (x[i]-20, y[i]-10), (x[i]-10, y[i]-20)], 3)
        pygame.draw.circle(screen, (200, 200, 200), (x[i]+20, y[i]), 5)
        pygame.draw.circle(screen, (200, 200, 200), (x[i]-10, y[i]), 5)
    start_time = current_time
    pygame.display.update()
    clock.tick(60)
    if 20 - int(current_time / 1000) <= 0 or keys[pygame.K_q]:
        keepGoing = False
        
screen.fill(BLACK)
strin = "Game Over! "
strin += "You were in "
strin += str(place)
if place == 1:
    strin += "st Place!"
elif place == 2:
    strin += "nd Place!"
elif place == 3:
    strin += "rd Place!"
else:
    strin += "th Place!"
text_three = pygame.font.SysFont("Arial", 60).render(strin, True, WHITE)
txtrect = text_three.get_rect()
txtrect.centerx = screen.get_rect().centerx
txtrect.y = 300
screen.blit(text_three, txtrect)
pygame.display.update()
time.sleep(5)
pygame.quit()

