import pygame
import random

# 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Typing Game!")
FONT = pygame.font.SysFont("malgun gothic", 48)
INPUT_FONT = pygame.font.SysFont("malgun gothic", 36)
TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER, 2000)
clock = pygame.time.Clock()

# 단어 리스트
words = ["about","accept","action","add","age","address","art","bar","behind","blue","brother","business",
         "car","cell","center","challenge","choice","common","deep","different","dinner","drop",
         "eat","effect","else","enter","expert","feeling","find","five","forward","give","ground",
         "happen","heart","hope","history","house","include","item","into","interest","inside","kitchen","large","language"]


# 게임 상태 변수
user_input = ""
score = 0
lives = 3
falling_words = []

def get_random_word():
  ran_words = random.choice(words)
  return ran_words
  
def add_falling_word():
  word = get_random_word()
  x = random.randint(50,600)
  y = 0
  speed = random.randint(2,5)
  falling_words.append ({"word":word,"x":x,"y":y,"speed":speed})
  
  
def update_words():
  for word in falling_words:
    word["y"] += word["speed"]
  

def check_input():
  global score, user_input
  for word in falling_words:
    if word["word"] == user_input:
      falling_words.remove(word)
      score += 10
      user_input = ""
      return True
  else :
    user_input = ""
    return False
  
def check_missed():
  global lives
  for word in falling_words:
    if word["y"] > 600:
      falling_words.remove(word)
      lives -= 1
      
def draw_words():
    for word in falling_words:
        text = FONT.render(word["word"], True, (255, 255, 255))
        screen.blit(text, (word["x"], word["y"]))
        
def draw_ui():
    draw_words()
    input_text = INPUT_FONT.render(f"입력: {user_input}", True, (0, 255, 0))
    score_text = INPUT_FONT.render(f"점수: {score}", True, (255, 255, 0))
    lives_text = INPUT_FONT.render(f"목숨: {lives}", True, (255, 100, 100))
    screen.blit(input_text, (20, 550))
    screen.blit(score_text, (650, 20))
    screen.blit(lives_text, (650, 60))

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TIMER:
            add_falling_word()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_RETURN:
                check_input()
            else:
                user_input += event.unicode

    update_words()
    check_missed()
    draw_ui()

    if lives <= 0:
        game_over_text = FONT.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (300, 250))
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()
